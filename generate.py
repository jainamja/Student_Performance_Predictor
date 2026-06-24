import pandas as pd
import random

data = []

for i in range(1000):

    study_hours = round(random.uniform(1, 10), 1)
    attendance = random.randint(40, 100)
    previous_scores = random.randint(30, 100)
    sleep_hours = round(random.uniform(4, 9), 1)

    internet_access = random.randint(0, 1)
    extra_activities = random.randint(0, 1)
    family_support = random.randint(0, 1)

    motivation_level = random.randint(1, 10)

    # Better performance formula
    performance = (
        study_hours * 3 +
        attendance * 0.2 +
        previous_scores * 0.3 +
        sleep_hours * 1 +
        motivation_level * 1.5
    )

    # Penalties
    if attendance < 60:
        performance -= 15

    if study_hours < 2:
        performance -= 20

    if previous_scores < 40:
        performance -= 15

    # Bonuses
    if internet_access == 1:
        performance += 3

    if family_support == 1:
        performance += 3

    if extra_activities == 1:
        performance += 1

    # Final score range
    performance = max(0, min(round(performance, 2), 100))

    data.append([
        study_hours,
        attendance,
        previous_scores,
        sleep_hours,
        internet_access,
        extra_activities,
        family_support,
        motivation_level,
        performance
    ])

columns = [
    'study_hours',
    'attendance',
    'previous_scores',
    'sleep_hours',
    'internet_access',
    'extra_activities',
    'family_support',
    'motivation_level',
    'performance'
]

df = pd.DataFrame(data, columns=columns)

# Save dataset
df.to_csv('student_data.csv', index=False)

print("Dataset generated successfully!")
print("File created: student_data.csv")