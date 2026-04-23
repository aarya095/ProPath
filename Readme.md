# ProPath: Intelligent Career Trajectory Modeling Using Machine Learning

## Overview

ProPath is a machine learning-based application that analyzes a user's skills, current job role, and experience to predict the next possible career role. It also recommends relevant skills and estimates career growth potential.

The system is designed as a lightweight MVP using FastAPI for the backend and Streamlit for the user interface.

---

## Features

* Predict next job role using machine learning
* Recommend trending skills based on data
* Estimate career growth category (High / Medium / Stable)
* Interactive user interface using Streamlit
* Downloadable career report

---

## Tech Stack

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas
* Joblib

---

## Project Structure

```
propath/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── model/
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── preprocess.py
│   │   ├── model.pkl
│   │   └── vectorizer.pkl
│   └── utils/
│
├── data/
│   └── dataset.csv
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/aarya095/ProPath.git
cd ProPath
```

---

### 2. Create Virtual Environment and activate it

#### For Windows

```
python -m venv venv
venv/Scripts/activate
```

#### For Bash

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---


### 4. Train the Model

```
python -m app.model.train
```

This will generate:

* model.pkl
* vectorizer.pkl

---

### 5. Run FastAPI Backend

Go back to root directory:

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

### 6. Run Streamlit Frontend

Open a new terminal:

```
streamlit run streamlit_app/app.py
```

---

## Usage

1. Enter skills, job title, and experience
2. Click "Generate Prediction"
3. View:

   * Predicted role
   * Growth category
   * Recommended skills
4. Download the generated report

---

## Important Notes

* Ensure FastAPI server is running before starting Streamlit
* Model must be trained before prediction
* Dataset should be clean and properly formatted

---

## Future Enhancements

* Integration with LinkedIn API
* Advanced ML models (Deep Learning)
* Improved recommendation system
* Deployment on cloud platforms

---

## Author

Aarya Sarfare

---
