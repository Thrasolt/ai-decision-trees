from DataModels.DataPoint import DECISION_TREES
from DataModels.fakeData import get_fake_dataframe

n = 1000

df = get_fake_dataframe(n, DECISION_TREES)
df.to_csv("ri_data.csv", sep=';')