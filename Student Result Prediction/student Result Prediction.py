import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("student_data.csv")

X = data[['StudyHours', 'Attendance', 'PreviousMarks']]

y = data['Result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy * 100, "%")

print("\nEnter Student Details")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance Percentage: "))
previous_marks = float(input("Previous Marks: "))

# Predict result
prediction = model.predict([[study_hours, attendance, previous_marks]])

print("\nPredicted Result:", prediction[0])