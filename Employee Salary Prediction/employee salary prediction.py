from sklearn.linear_model import LinearRegression
import numpy as np

print("Program started...")

experience = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
salary = np.array([30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000])

model = LinearRegression()
model.fit(experience, salary)

print("Model trained successfully!")

exp = float(input("Enter years of experience: "))

predicted_salary = model.predict([[exp]])

print("Predicted Salary: Rs.", round(predicted_salary[0], 2))

input("\nPress Enter to exit...")