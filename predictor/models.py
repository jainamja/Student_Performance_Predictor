from django.db import models

class Prediction(models.Model):

    study_hours = models.FloatField()
    attendance = models.FloatField()
    previous_scores = models.FloatField()
    sleep_hours = models.FloatField()

    internet_access = models.IntegerField()
    extra_activities = models.IntegerField()
    family_support = models.IntegerField()

    motivation_level = models.IntegerField()

    prediction = models.FloatField()

    category = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id}"