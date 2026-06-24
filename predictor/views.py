from django.shortcuts import render
import joblib
import numpy as np
from .models import Prediction
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Load trained model
model = joblib.load('predictor/student_model.pkl')


def home(request):
    return render(request, 'predictor/home.html')


def predict(request):

    prediction = None
    category = None
    suggestion = None

    if request.method == "POST":

        study_hours = float(request.POST.get('study_hours'))
        attendance = float(request.POST.get('attendance'))
        previous_scores = float(request.POST.get('previous_scores'))
        sleep_hours = float(request.POST.get('sleep_hours'))

        internet_access = int(request.POST.get('internet_access'))
        extra_activities = int(request.POST.get('extra_activities'))
        family_support = int(request.POST.get('family_support'))

        motivation_level = int(request.POST.get('motivation_level'))

        features = np.array([[
            study_hours,
            attendance,
            previous_scores,
            sleep_hours,
            internet_access,
            extra_activities,
            family_support,
            motivation_level
        ]])

        result = model.predict(features)

        prediction = round(result[0], 2)

        # Categories
        if prediction >= 85:
            category = "Excellent 🌟"
            suggestion = "Keep maintaining your excellent performance."

        elif prediction >= 70:
            category = "Good 👍"
            suggestion = "You are doing well. Focus more on consistency."

        elif prediction >= 50:
            category = "Average 📘"
            suggestion = "Increase study hours and improve attendance."

        else:
            category = "Needs Improvement ⚠️"
            suggestion = "Focus on daily study routine and seek guidance."
        
        # Save prediction to database
        Prediction.objects.create(
            study_hours=study_hours,
            attendance=attendance,
            previous_scores=previous_scores,
            sleep_hours=sleep_hours,
            internet_access=internet_access,
            extra_activities=extra_activities,
            family_support=family_support,
            motivation_level=motivation_level,
            prediction=prediction,
            category=category
        )

    return render(request, 'predictor/predict.html', {
        'prediction': prediction,
        'category': category,
        'suggestion': suggestion
    })
def history(request):

    predictions = Prediction.objects.all().order_by('-created_at')

    total_predictions = predictions.count()

    average_prediction = predictions.aggregate(
        Avg('prediction')
    )['prediction__avg']

    excellent_count = predictions.filter(
        category="Excellent 🌟"
    ).count()

    good_count = predictions.filter(
        category="Good 👍"
    ).count()

    average_count = predictions.filter(
        category="Average 📘"
    ).count()

    low_count = predictions.filter(
        category="Needs Improvement ⚠️"
    ).count()

    context = {
        'predictions': predictions,
        'total_predictions': total_predictions,
        'average_prediction': round(average_prediction or 0, 2),
        'excellent_count': excellent_count,
        'good_count': good_count,
        'average_count': average_count,
        'low_count': low_count,
    }

    return render(request, 'predictor/history.html', context)

def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'predictor/register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('/login/')

    return render(request, 'predictor/register.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/predict/')

        else:

            return render(request, 'predictor/login.html', {
                'error': 'Invalid Username or Password'
            })

    return render(request, 'predictor/login.html')


def logout_view(request):

    logout(request)

    return redirect('/login/')