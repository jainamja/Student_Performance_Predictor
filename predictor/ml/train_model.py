import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Get base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CSV path
csv_path = os.path.join(BASE_DIR, 'student_data.csv')

# Load dataset
data = pd.read_csv(csv_path)

print("Dataset Loaded Successfully!")
print(data.head())

# Features
X = data[
    [
        'study_hours',
        'attendance',
        'previous_scores',
        'sleep_hours',
        'internet_access',
        'extra_activities',
        'family_support',
        'motivation_level'
    ]
]

# Target
y = data['performance']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy scores
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Training Completed!")
print(f"Mean Absolute Error: {mae}")
print(f"R2 Score: {r2}")

# Save model path
model_path = os.path.join(BASE_DIR, 'predictor', 'student_model.pkl')

# Save model
joblib.dump(model, model_path)

print("\nModel saved successfully!")
print(f"Model path: {model_path}")