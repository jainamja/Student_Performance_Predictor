# Student Performance Predictor

A Django web application that predicts student academic performance using a machine learning model trained on key student attributes.

---

## Features

- Predict student performance score based on study habits and personal factors
- Categorizes results as Excellent, Good, Average, or Needs Improvement
- Saves prediction history to a database with stats and averages
- User registration and login system
- Clean, simple web interface

---

## Tech Stack

- **Backend:** Django 5.0.14
- **ML Model:** Scikit-learn (Linear Regression)
- **Data Handling:** Pandas, NumPy
- **Model Persistence:** Joblib
- **Database:** SQLite3

---

## Project Structure

```
Student_Performance_Predictor/
└── student_performance_predictor/
    ├── manage.py
    ├── student_data.csv
    ├── generate.py
    ├── db.sqlite3
    ├── predictor/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   ├── student_model.pkl
    │   ├── ml/
    │   │   └── train_model.py
    │   └── templates/
    │       └── predictor/
    │           ├── home.html
    │           ├── predict.html
    │           ├── history.html
    │           ├── login.html
    │           └── register.html
    └── student_performance_predictor/
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── asgi.py
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Student_Performance_Predictor/student_performance_predictor
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## ML Model

The model is a **Linear Regression** trained on the following input features:

| Feature | Description |
|---|---|
| `study_hours` | Hours spent studying per day |
| `attendance` | Attendance percentage |
| `previous_scores` | Previous academic scores |
| `sleep_hours` | Hours of sleep per night |
| `internet_access` | Whether student has internet access (0/1) |
| `extra_activities` | Participation in extra activities (0/1) |
| `family_support` | Family support availability (0/1) |
| `motivation_level` | Motivation level (scale 1–10) |

**Output:** A predicted performance score (0–100)

### Performance Categories

| Score | Category |
|---|---|
| 85 – 100 | Excellent 🌟 |
| 70 – 84 | Good 👍 |
| 50 – 69 | Average 📘 |
| Below 50 | Needs Improvement ⚠️ |

### Retrain the Model (Optional)

To regenerate the dataset and retrain:

```bash
# Generate a fresh dataset
python generate.py

# Train and save the model
python predictor/ml/train_model.py
```

---

## Pages

| URL | Description |
|---|---|
| `/` | Home page |
| `/predict/` | Enter student data and get a prediction |
| `/history/` | View all past predictions with stats |
| `/register/` | Register a new user account |
| `/login/` | Log in |
| `/logout/` | Log out |

---

## Deployment Notes

- Set `DEBUG = False` in `settings.py` before deploying to production
- Replace the default `SECRET_KEY` with a secure, randomly generated key
- For production, consider switching from SQLite to PostgreSQL
- Run `python manage.py collectstatic` if serving static files via a web server

---

## Requirements

See [requirements.txt](requirements.txt) for the full list of dependencies.
