from visualization.VisualizeResults import VisualizeResults, RULE_INDUCTION, DECISION_TREES, RANDOM_FORESTS

vri = VisualizeResults("../DataModels/ri_data.csv", RULE_INDUCTION)
vri.show_plotting()

vdt = VisualizeResults("../DataModels/dt_data.csv", DECISION_TREES)
vdt.show_plotting()

vrf = VisualizeResults("../DataModels/rf_data.csv", RANDOM_FORESTS)
vrf.show_plotting()
