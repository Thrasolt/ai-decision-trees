from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from data_mod.fakeData import get_fake_dataframe

df = get_fake_dataframe(1000000)

X = df.values[:, :-1]
Y = df.values[:, -1]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.3, random_state=100)

clf_entropy = DecisionTreeClassifier(criterion="entropy")
clf_entropy.fit(X_train, y_train)

y_pred = clf_entropy.predict(X_test)

print(f"Accuracy is {accuracy_score(y_test, y_pred) * 100}")

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(f"Accuracy is {accuracy_score(y_test, y_pred) * 100}")