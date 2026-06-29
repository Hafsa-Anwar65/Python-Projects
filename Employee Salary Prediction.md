# Employee Salary Prediction using Linear Regression

A simple Machine Learning project built with **Python** and **Scikit-learn** that predicts an employee's salary based on years of experience using the **Linear Regression** algorithm.

---

## Features

- Predicts salary based on experience
- Uses Linear Regression from Scikit-learn
- Beginner-friendly code
- Command-line interface
- Easy to understand and modify

---

## Technologies Used

- Python 3.x
- NumPy
- Scikit-learn

---

## Installation

1. Clone this repository

```bash
git clone https://github.com/yourusername/employee-salary-prediction.git
```

2. Navigate to the project folder

```bash
cd employee-salary-prediction
```

3. Install the required libraries

```bash
pip install numpy scikit-learn
```

---

## How to Run

Run the Python file:

```bash
python employee_salary_prediction.py
```

The program will ask for the employee's years of experience.

Example:

```
Program started...
Model trained successfully!

Enter years of experience: 5
```

Output:

```
Predicted Salary: Rs. 50000
```

---

## Dataset

The project uses a small sample dataset for demonstration.

| Experience (Years) | Salary (Rs.) |
|-------------------:|-------------:|
| 1 | 30000 |
| 2 | 35000 |
| 3 | 40000 |
| 4 | 45000 |
| 5 | 50000 |
| 6 | 55000 |
| 7 | 60000 |
| 8 | 65000 |

---

## Machine Learning Model

The project uses the **Linear Regression** algorithm.

The model learns the relationship between:

- **Input:** Years of Experience
- **Output:** Employee Salary

After training, it predicts the expected salary for any experience entered by the user.

---

## Project Structure

```
employee-salary-prediction/
│
├── employee_salary_prediction.py
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.10 or later
- NumPy
- Scikit-learn

Install dependencies:

```bash
pip install numpy scikit-learn
```

---

## Future Improvements

- Train on a real-world salary dataset
- Add data visualization using Matplotlib
- Create a web interface using Flask or Streamlit
- Improve prediction accuracy with larger datasets
- Save and load the trained model using Joblib

---

## Learning Objectives

This project demonstrates:

- Linear Regression
- Machine Learning basics
- Model training and prediction
- NumPy array manipulation
- User input handling in Python

---

## License

This project is open source and available under the MIT License.
