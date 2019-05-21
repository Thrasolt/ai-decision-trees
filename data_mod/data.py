from data_mod.fakeData import get_fake_dataframe

df = get_fake_dataframe(1000)

df.to_csv("data_mod.csv", sep=',')



