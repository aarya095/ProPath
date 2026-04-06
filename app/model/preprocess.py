from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    return TfidfVectorizer()

def preprocess_data(df, vectorizer):
    df['combined'] = (
        df['skills'].str.lower() + " " +
        df['current_job_title'].str.lower() + " " +
        df['years_of_experience'].astype(str)
    )

    X = vectorizer.fit_transform(df['combined'])
    return X, df

def transform_input(skills, job_title, experience, vectorizer):
    combined = f"{skills.lower()} {job_title.lower()} {experience}"
    return vectorizer.transform([combined])