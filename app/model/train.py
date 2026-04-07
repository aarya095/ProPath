import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib
from app.model.preprocess import preprocess_data, create_vectorizer

df = pd.read_csv("data/dataset.csv")

vectorizer = create_vectorizer()

X, df = preprocess_data(df, vectorizer)
y = df['next_job_role']

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

model = LogisticRegression()
model.fit(X, y_encoded)

# Save model, label_encoder, and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model, vectorizer, and label encoder saved!")