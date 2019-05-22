from data_mod.DataPoint import RULE_INDUCTION, DECISION_TREES
from data_mod.fakeData import get_fake_dataframe

n = 1000

df = get_fake_dataframe(n, RULE_INDUCTION)
df.to_csv("ri_data.csv", sep=',')

df = get_fake_dataframe(n, DECISION_TREES)
df.to_csv("dt_data.csv", sep=',')

df = get_fake_dataframe(n)
df.to_csv("rf_data.csv", sep=',')




