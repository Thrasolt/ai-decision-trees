import DataModels.DataPoint
from DataModels.fakeData import get_fake_dataframe

n = 50000

df = get_fake_dataframe(n, DataModels.DataPoint.RANDOM_FORESTS)
df.to_csv("rf_data.csv", sep=',')
