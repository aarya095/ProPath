from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    return TfidfVectorizer()

def preprocess_data(df, vectorizer):
    df['skills'] = df['skills'].str.lower()
    X = vectorizer.fit_transform(df['skills'])
    return X, df

def transform_input(
        skills, 
        vectorizer
        ):
    return vectorizer.transform([skills.lower()])