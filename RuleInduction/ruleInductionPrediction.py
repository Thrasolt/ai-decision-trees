import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import RuleInduction.model as model

df = pd.read_csv("ri_data_new.csv")

X = df.values[:, :-1]  # Features
Y = df.values[:, -1]  # Classess

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

y_pred = model.predict(X_test)
print(f"Rule Induction Accuracy is {accuracy_score(y_test, y_pred) * 100:.2f}%")