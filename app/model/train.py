import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from app.model.preprocess import preprocess_data, create_vectorizer

df = pd.read_csv("data/dataset.csv")

vectorizer = create_vectorizer()

X, df = preprocess_data(df, vectorizer)
y = df['next_job_role']

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)
model.fit(X, y)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved!")

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))