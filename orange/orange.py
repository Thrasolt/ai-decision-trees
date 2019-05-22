import Orange
data = Orange.data.Table('data_mod.csv')
#disc = Orange.preprocess.Discretize()
#disc.method = Orange.preprocess.discretize.EqualWidth(n=6)
#data = disc(data)
learner = Orange.classification.CN2UnorderedLearner()
classifier = learner(data)
learner.rule_finder.search_strategy.bound_continuous = True
learner.rule_finder.general_validator.max_rule_length = 3 
learner.rule_finder.general_validator.min_covered_examples = 100
for rule in classifier.rule_list:
    print(rule, rule.curr_class_dist.tolist())


