from visualization.VisualizeResults import VisualizeResults, RULE_INDUCTION, DECISION_TREES, RANDOM_FORESTS

vri = VisualizeResults("ri_data.csv", RULE_INDUCTION)
vri.show_plotting()

vdt = VisualizeResults("dt_data.csv", DECISION_TREES)
vdt.show_plotting()

vrf = VisualizeResults("rf_data.csv", RANDOM_FORESTS)
vrf.show_plotting()
