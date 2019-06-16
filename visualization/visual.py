import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_initial = pd.read_csv('../DataModels/DataModels.csv', index_col=0)


def bars(df):
    df = df.mean()
    df.plot.bar(stacked=True)
    plt.show()


def curves(df):
    df.cumsum()
    df.plot()
    plt.show()

curves(df_initial)

