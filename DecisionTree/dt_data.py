from RandomForest import rf_data
from DataModels.DataPoint import DECISION_TREES
from DataModels.fakeData import get_fake_dataframe

n = 50000

df = get_fake_dataframe(n, DECISION_TREES)
df.to_csv("dt_data.csv", sep=',')
