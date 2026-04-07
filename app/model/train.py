import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from app.model.preprocess import preprocess_data, create_vectorizer

df = pd.read_csv("data/dataset.csv")

vectorizer = create_vectorizer()

X, df = preprocess_data(df, vectorizer)
y = df['next_job_role']

model = LogisticRegression()
model.fit(X, y)

# Save BOTH model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved!")