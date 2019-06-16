from data_mod.DataPoint import DECISION_TREES
from data_mod.fakeData import get_fake_dataframe

n = 50000

df = get_fake_dataframe(n, DECISION_TREES)
df.to_csv("dt_data.csv", sep=',')
