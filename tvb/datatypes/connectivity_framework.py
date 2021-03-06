# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#
"""
Framework methods for the Connectivity datatype.

.. moduleauthor:: Lia Domide <lia.domide@codemart.ro>
.. moduleauthor:: Stuart A. Knock <Stuart@tvb.invalid>
"""

import numpy
import tvb.datatypes.connectivity_data as connectivity_data


class ConnectivityFramework(connectivity_data.ConnectivityData):
    """ 
    This class exists to add framework methods and attributes to Connectivity.
    """
    
    __tablename__ = None

    @property
    def display_name(self):
        """
        Overwrite from superclass and add number of regions field (as title on DataStructure tree)
        """
        previous = super(ConnectivityFramework, self).display_name or "Connectivity"
        return previous + " " + str(self.number_of_regions)
    

    def branch_connectivity(self, new_weights, interest_areas, storage_path, new_tracts=None):
        """
        Generate new Connectivity based on current one, by changing weights (e.g. simulate lesion).
        The returned connectivity has the same number of nodes. The edges of unselected nodes will have weight 0.
        :param new_weights: weights matrix for the new connectivity
        :param interest_areas: ndarray of the selected node id's
        :param new_tracts: tracts matrix for the new connectivity
        """
        if new_tracts is None:
            new_tracts = self.tract_lengths

        for i in xrange(len(self.weights)):
            for j in xrange(len(self.weights)):
                if i not in interest_areas or j not in interest_areas:
                    new_weights[i][j] = 0

        final_conn = self.__class__()
        final_conn.parent_connectivity = self.gid
        final_conn.storage_path = storage_path
        final_conn.weights = new_weights
        final_conn.centres = self.centres
        final_conn.region_labels = self.region_labels
        final_conn.orientations = self.orientations
        final_conn.cortical = self.cortical
        final_conn.hemispheres = self.hemispheres
        final_conn.areas = self.areas
        final_conn.tract_lengths = new_tracts
        final_conn.saved_selection = interest_areas.tolist()
        final_conn.subject = self.subject
        return final_conn


    def cut_connectivity(self, new_weights, interest_areas, storage_path, new_tracts=None):
        """
        Generate new Connectivity object based on current one, by removing nodes (e.g. simulate lesion).
        Only the selected nodes will get used in the result. The order of the indices in interest_areas matters.
        If indices are not sorted then the nodes will be permuted accordingly.
        :param new_weights: weights matrix for the new connectivity
        :param interest_areas: ndarray with the selected node id's.
        :param new_tracts: tracts matrix for the new connectivity
        """
        if new_tracts is None:
            new_tracts = self.tract_lengths[interest_areas, :][:, interest_areas]
        else:
            new_tracts = new_tracts[interest_areas, :][:, interest_areas]
        new_weights = new_weights[interest_areas, :][:, interest_areas]

        final_conn = self.__class__()
        final_conn.parent_connectivity = None
        final_conn.storage_path = storage_path
        final_conn.weights = new_weights
        final_conn.centres = self.centres[interest_areas, :]
        final_conn.region_labels = self.region_labels[interest_areas]
        if self.orientations is not None and len(self.orientations):
            final_conn.orientations = self.orientations[interest_areas, :]
        if self.cortical is not None and len(self.cortical):
            final_conn.cortical = self.cortical[interest_areas]
        final_conn.hemispheres = self.hemispheres[interest_areas]
        final_conn.areas = self.areas[interest_areas]
        final_conn.tract_lengths = new_tracts
        final_conn.saved_selection = None
        final_conn.subject = self.subject
        return final_conn


    def _reorder_arrays(self, new_weights, interest_areas, new_tracts=None):
        """
        Returns ordered versions of the parameters according to the hemisphere permutation.
        """
        permutation = self.hemisphere_order_indices
        inverse_permutation = numpy.argsort(permutation)  # trick to invert a permutation represented as an array
        interest_areas = inverse_permutation[interest_areas]
        # see :meth"`ordered_weights` for why [p:][:p]
        new_weights = new_weights[inverse_permutation, :][:, inverse_permutation]

        if new_tracts is not None:
            new_tracts = new_tracts[inverse_permutation, :][:, inverse_permutation]

        return new_weights, interest_areas, new_tracts


    def branch_connectivity_from_ordered_arrays(self, new_weights, interest_areas, storage_path, new_tracts=None):
        """
        Similar to :meth:`branch_connectivity` but the parameters are consistent with the ordered versions of weights, tracts, labels
        Used by the connectivity viewer to save a lesion.
        """
        new_weights, interest_areas, new_tracts = self._reorder_arrays(new_weights, interest_areas, new_tracts)
        return self.branch_connectivity(new_weights, interest_areas, storage_path, new_tracts)


    def cut_new_connectivity_from_ordered_arrays(self, new_weights, interest_areas, storage_path, new_tracts=None):
        """
        Similar to :meth:`cut_connectivity` but using hemisphere ordered parameters.
        Used by the connectivity viewer to save a smaller connectivity.
        """
        new_weights, interest_areas, new_tracts = self._reorder_arrays(new_weights, interest_areas, new_tracts)
        return self.cut_connectivity(new_weights, interest_areas, storage_path, new_tracts)


    @property
    def saved_selection_labels(self):
        """
        Taking the entity field saved_selection, convert indexes in that array
        into labels.
        """
        if self.saved_selection:
            idxs = [int(i) for i in self.saved_selection]
            result = ''
            for i in idxs:
                result += self.region_labels[i] + ','
            return result[:-1]
        else:
            return ''


    @staticmethod  
    def accepted_filters():
        filters = connectivity_data.ConnectivityData.accepted_filters()
        filters.update({'datatype_class._number_of_regions': {'type': 'int', 'display': 'No of Regions',
                                                              'operations': ['==', '<', '>']}})
        return filters


    def is_right_hemisphere(self, idx):
        """
        :param idx:  Region IDX
        :return: True when hemispheres information is present and it shows that the current node is in the right
        hemisphere. When hemispheres info is not present, return True for the second half of the indices and
        False otherwise.
        """
        if self.hemispheres is not None and self.hemispheres.size:
            return self.hemispheres[idx]
        return idx >= self.number_of_regions / 2


    @property
    def hemisphere_order_indices(self):
        """
        A sequence of indices of rows/colums.
        These permute rows/columns so that the first half would belong to the first hemisphere
        If there is no hemisphere information returns the identity permutation
        """
        if self.hemispheres is not None and self.hemispheres.size:
            li, ri = [], []
            for i, is_right in enumerate(self.hemispheres):
                if is_right:
                    ri.append(i)
                else:
                    li.append(i)
            return numpy.array(li + ri)
        else:
            return numpy.arange(self.number_of_regions)


    @property
    def ordered_weights(self):
        """
        This view of the weights matrix lists all left hemisphere nodes before the right ones.
        It is used by viewers of the connectivity.
        """
        permutation = self.hemisphere_order_indices
        # how this works:
        # w[permutation, :] selects all rows at the indices present in the permutation array thus permuting the rows
        # [:, permutation] does the same to columns. See numpy index arrays
        return self.weights[permutation, :][:, permutation]

    @property
    def ordered_tracts(self):
        """
        Similar to :meth:`ordered_weights`
        """
        permutation = self.hemisphere_order_indices
        return self.tract_lengths[permutation, :][:, permutation]

    @property
    def ordered_labels(self):
        """
        Similar to :meth:`ordered_weights`
        """
        permutation = self.hemisphere_order_indices
        return self.region_labels[permutation]

    @property
    def ordered_centres(self):
        """
        Similar to :method:`ordered_weights`
        """
        permutation = self.hemisphere_order_indices
        return self.centres[permutation]

    def get_grouped_space_labels(self):
        """
        :return: A list [('left', [lh_labels)], ('right': [rh_labels])]
        """
        if self.hemispheres is not None and self.hemispheres.size:
            l, r = [], []

            for i, (is_right, label) in enumerate(zip(self.hemispheres, self.region_labels)):
                if is_right:
                    r.append((i, label))
                else:
                    l.append((i, label))
            return [('left', l), ('right', r)]
        else:
            return [('', list(enumerate(self.region_labels)))]


    def get_default_selection(self):
        # should this be sub-selection or all always?
        sel = self.saved_selection
        if sel is not None:
            return sel
        else:
            return range(len(self.region_labels))


    def get_measure_points_selection_gid(self):
        """
        :return: the associated connectivity gid
        """
        return self.gid


    @property
    def binarized_weights(self):
        """
        :return: a matrix of he same size as weights, with 1 where weight > 0, and 0 in rest
        """
        result = numpy.zeros_like(self.weights)
        result = numpy.where(self.weights > 0, 1, result)
        return result

