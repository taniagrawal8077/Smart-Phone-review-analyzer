import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# load dataset
df = pd.read_csv("dataset.csv")

# convert aspect column into list
df['aspect'] = df['aspect'].apply(lambda x: x.split(","))

# vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])

# multi-label encoding
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(df['aspect'])

# model
model = OneVsRestClassifier(LogisticRegression(max_iter=1000))
model.fit(X, y)

# prediction function
def predict_aspects(text):
    X_input = vectorizer.transform([text])
    pred = model.predict(X_input)
    aspects = mlb.inverse_transform(pred)
    return list(aspects[0]) if aspects else []