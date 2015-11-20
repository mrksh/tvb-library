class LayeredMicrocircuit(Model):
    r"""
    [TODO]
    """

    _ui_name = "CorticalColumn"
    ui_configurable_parameters = ["Iext", "Iext2", "r", "x0", "slope"]

    l2E_to_l2E = arrays.FloatArray(
        label="l2E_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l2I = arrays.FloatArray(
        label="l2E_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l4E = arrays.FloatArray(
        label="l2E_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l4I = arrays.FloatArray(
        label="l2E_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l5E = arrays.FloatArray(
        label="l2E_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l5I = arrays.FloatArray(
        label="l2E_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l6E = arrays.FloatArray(
        label="l2E_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2E_to_l6I = arrays.FloatArray(
        label="l2E_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)

    l2I_to_l2E = arrays.FloatArray(
        label="l2I_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l2I = arrays.FloatArray(
        label="l2I_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l4E = arrays.FloatArray(
        label="l2I_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l4I = arrays.FloatArray(
        label="l2I_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l5E = arrays.FloatArray(
        label="l2I_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l5I = arrays.FloatArray(
        label="l2I_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l6E = arrays.FloatArray(
        label="l2I_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l2I_to_l6I = arrays.FloatArray(
        label="l2I_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)


    ################################
    ################################
    ################################

    l4E_to_l2E = arrays.FloatArray(
        label="l4E_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l2I = arrays.FloatArray(
        label="l4E_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l4E = arrays.FloatArray(
        label="l4E_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l4I = arrays.FloatArray(
        label="l4E_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l5E = arrays.FloatArray(
        label="l4E_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l5I = arrays.FloatArray(
        label="l4E_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l6E = arrays.FloatArray(
        label="l4E_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4E_to_l6I = arrays.FloatArray(
        label="l4E_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)

    l4I_to_l2E = arrays.FloatArray(
        label="l4I_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l2I = arrays.FloatArray(
        label="l4I_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l4E = arrays.FloatArray(
        label="l4I_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l4I = arrays.FloatArray(
        label="l4I_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l5E = arrays.FloatArray(
        label="l4I_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l5I = arrays.FloatArray(
        label="l4I_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l6E = arrays.FloatArray(
        label="l4I_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l4I_to_l6I = arrays.FloatArray(
        label="l4I_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)


    ################################
    ################################
    ################################

    l5E_to_l2E = arrays.FloatArray(
        label="l5E_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5E_to_l2I = arrays.FloatArray(
        label="l5E_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5E_to_l4E = arrays.FloatArray(
        label="l5E_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5E_to_l4I = arrays.FloatArray(
        label="l5E_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5E_to_l5E = arrays.FloatArray(
        label="l5E_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5E_to_l5I = arrays.FloatArray(
        label="l5E_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5E_to_l6E = arrays.FloatArray(
        label="l5E_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)

    l5I_to_l2E = arrays.FloatArray(
        label="l5I_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l2I = arrays.FloatArray(
        label="l5I_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l4E = arrays.FloatArray(
        label="l5I_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l4I = arrays.FloatArray(
        label="l5I_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l5E = arrays.FloatArray(
        label="l5I_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l5I = arrays.FloatArray(
        label="l5I_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l6E = arrays.FloatArray(
        label="l5I_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l5I_to_l6I = arrays.FloatArray(
        label="l5I_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)

    ################################
    ################################
    ################################

    l6E_to_l2E = arrays.FloatArray(
        label="l6E_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l2I = arrays.FloatArray(
        label="l6E_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l4E = arrays.FloatArray(
        label="l6E_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l4I = arrays.FloatArray(
        label="l6E_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l5E = arrays.FloatArray(
        label="l6E_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l5I = arrays.FloatArray(
        label="l6E_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l6E = arrays.FloatArray(
        label="l6E_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6E_to_l6I = arrays.FloatArray(
        label="l6E_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)


    ################################
    ################################
    ################################

    l6I_to_l2E = arrays.FloatArray(
        label="l6I_to_l2E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l2I = arrays.FloatArray(
        label="l6I_to_l2I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l4E = arrays.FloatArray(
        label="l6I_to_l4E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l4I = arrays.FloatArray(
        label="l6I_to_l4I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l5E = arrays.FloatArray(
        label="l6I_to_l5E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l5I = arrays.FloatArray(
        label="l6I_to_l5I",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l6E = arrays.FloatArray(
        label="l6I_to_l6E",
        default=numpy.array([1]),
        doc="",
        order=-1)
    l6I_to_l6I = arrays.FloatArray(
        label="l6I_to_l6I",
        default=numpy.array([1]),
        doc="",
        order=-1)


    ################################
    ################################
    ################################

    KE = arrays.FloatArray(
        label="KE",
        default=numpy.array([0.21]),
        doc="Efficacy of local excitatory coupling",
        order=0)
    KI = arrays.FloatArray(
        label="KI",
        default=numpy.array([0.21]),
        doc="Efficacy of local inhibitory coupling",
        order=1)

    I_BG = arrays.FloatArray(
        label="I_BG",
        default=numpy.array([1]),
        doc="Background stimulation",
        order=2)

    I_LGN = arrays.FloatArray(
        label="I_LGN",
        default=numpy.array([2]),
        doc="LGN input",
        order=3)

    delay = arrays.FloatArray(
        label="delay",
        default=numpy.array([0.1]),
        doc="Local transmission delay",
        order=4)

    ######################################################################
    ######################################################################
    ######################################################################

    state_variable_range = basic.Dict(
        label="State variable ranges [lo, hi]",
        default={"rL2E": numpy.array([0, 100]),
                 "rL2I": numpy.array([0, 100]),
                 "rL4E": numpy.array([0, 100]),
                 "rL4I": numpy.array([0, 100]),
                 "rL5E": numpy.array([0, 100]),
                 "rL5I": numpy.array([0, 100]),
                 "rL6E": numpy.array([0, 100])
                 "rL6I": numpy.array([0, 100])
             },
        doc="n/a",
        order=-1
        )

    variables_of_interest = basic.Enumerate(
        label="Variables watched by Monitors",
        options=["rL2E", "rL2I", "rL4E", "rL4I", "rL5E", "rL5I", "rL6E", "rL6I"],
        default=["rL2E", "rL4E", "rL5E", "rL6E"],
        select_multiple=True,
        doc="""default state variables to be monitored""",
        order=-1)

    ######################################################################
    ######################################################################
    ######################################################################


    def __init__(self, **kwargs):
        """
        """

        LOG.info("%s: init'ing..." % (str(self),))

        super(CorticalColumn, self).__init__(**kwargs)

        self._nvar = 8
        #??? self.cvar = numpy.array([0, 3], dtype=numpy.int32)

        LOG.info("%s: init'ed." % (repr(self),))

    def configure(self):
        self.local_coupling_matrix = np.array([
            [self.l2E_to_l2E, self.l2I_to_l2E, self.l4E_to_l2E, self.l4I_to_l2E, self.l5E_to_l2E, self.l5I_to_l2E, self.l6E_to_l2E, self.l6I_to_l2E],
            [self.l2E_to_l2I, self.l2I_to_l2I, self.l4E_to_l2I, self.l4I_to_l2I, self.l5E_to_l2I, self.l5I_to_l2I, self.l6E_to_l2I, self.l6I_to_l2I]
            [self.l2E_to_l4E, self.l2I_to_l4E, self.l4E_to_l4E, self.l4I_to_l4E, self.l5E_to_l4E, self.l5I_to_l4E, self.l6E_to_l4E, self.l6I_to_l4E],
            [self.l2E_to_l4I, self.l2I_to_l4I, self.l4E_to_l4I, self.l4I_to_l4I, self.l5E_to_l4I, self.l5I_to_l4I, self.l6E_to_l4I, self.l6I_to_l4I],
            [self.l2E_to_l5E, self.l2I_to_l5E, self.l4E_to_l5E, self.l4I_to_l5E, self.l5E_to_l5E, self.l5I_to_l5E, self.l6E_to_l5E, self.l6I_to_l5E],
            [self.l2E_to_l5I, self.l2I_to_l5I, self.l4E_to_l5I, self.l4I_to_l5I, self.l5E_to_l5I, self.l5I_to_l5I, self.l6E_to_l5I, self.l6I_to_l5I],
            [self.l2E_to_l6E, self.l2I_to_l6E, self.l4E_to_l6E, self.l4I_to_l6E, self.l5E_to_l6E, self.l5I_to_l6E, self.l6E_to_l6E, self.l6I_to_l6E],
            [self.l2E_to_l6I, self.l2I_to_l6I, self.l4E_to_l6I, self.l4I_to_l6I, self.l5E_to_l6I, self.l5I_to_l6I, self.l6E_to_l6I, self.l6I_to_l6I],
        ])
        self.local_coupling_matrix = self.local_coupling.matrix.dot(np.diag(self.KE, self.KI, self.KE, self.KI, self.KE, self.KI, self.KE, self.KI))

        # HOW to add stimulation? to which nodes?
        self.Iext = self.I_BG

    def dfun(self, state_variables, coupling, local_coupling=0.0,
             array=numpy.array, where=numpy.where, concat=numpy.concatenate):
        r"""
        """

        y = state_variables
        ydot = numpy.empty_like(state_variables)

        # maybe allow different input-output-function than max(0,.)?
        ydot = -y + np.maximum(0, self.Iext + self.local_coupling_matrix.dot(self.history[LOCAL_DELAY_STEPS]) + LONGRANGECOUPLING)

        return ydot