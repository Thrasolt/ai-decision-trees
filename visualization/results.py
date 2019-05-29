from visualization.VisualizeResults import VisualizeResults, RULE_INDUCTION, DECISION_TREES, RANDOM_FORESTS

vri = VisualizeResults("../data_mod/ri_data.csv", RULE_INDUCTION)
vri.show_plotting()

vdt = VisualizeResults("../data_mod/dt_data.csv", DECISION_TREES)
vdt.show_plotting()

vrf = VisualizeResults("../data_mod/rf_data.csv", RANDOM_FORESTS)
vrf.show_plotting()
