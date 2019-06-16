import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("rf_data.csv")

X = df.values[:, :-1]  # Features
Y = df.values[:, -1]  # Classes

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

dt_clf = RandomForestClassifier(n_estimators=100)
dt_clf.fit(X_train, y_train)

y_pred = dt_clf.predict(X_test)

print(f"Random Forest Prediction Accuracy is {accuracy_score(y_test, y_pred) * 100:.2f}%")
