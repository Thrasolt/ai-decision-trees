import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("dt_data.csv")


"""
df = pd.read_csv("data_mod.csv")
"""

X = df.values[:, :-1]  # Features
Y = df.values[:, -1]  # Classes

print(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

dt_clf = DecisionTreeClassifier(criterion="entropy")
dt_clf.fit(X_train, y_train)

y_pred = dt_clf.predict(X_test)

print(f"Decision Tree Accuracy is {accuracy_score(y_test, y_pred) * 100:.2f}%")
rf_clf = RandomForestClassifier(n_estimators=100)
rf_clf.fit(X_train, y_train)
y_pred = rf_clf.predict(X_test)
print(f"Random Forest Accuracy is {accuracy_score(y_test, y_pred) * 100:.2f}%")
