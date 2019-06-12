import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from data_mod.DataPoint import RULE_INDUCTION
from data_mod.fakeData import get_fake_dataframe


df = pd.read_csv("ri_data.csv")

X = df.values[:, :-1]  # Features
Y = df.values[:, -1]  # Classes

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)


############
dt_clf = DecisionTreeClassifier(criterion="entropy")
dt_clf.fit(X_train, y_train)

y_pred = dt_clf.predict(X_test)
###########

print(y_pred)

print(f"Decision Tree Accuracy is {accuracy_score(y_test, y_pred) * 100}%")

rf_clf = RandomForestClassifier(n_estimators=100)
rf_clf.fit(X_train, y_train)
y_pred = rf_clf.predict(X_test)

print(f"Random Forest Accuracy is {accuracy_score(y_test, y_pred) * 100}%")
