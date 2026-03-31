import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dataset.csv")

le_issue = LabelEncoder()
le_severity = LabelEncoder()

df["issue"] = le_issue.fit_transform(df["issue"])
df["severity"] = le_severity.fit_transform(df["severity"])

model = DecisionTreeClassifier()
model.fit(df[["issue"]], df["severity"])

def predict_severity(issue):
    issue_encoded = le_issue.transform([issue])
    pred = model.predict([issue_encoded])
    return le_severity.inverse_transform(pred)[0]