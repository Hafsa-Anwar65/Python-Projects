# Age Group Prediction System

print("=== Age Detection Model ===")

age = int(input("Enter age: "))

groups = {
    "Child": range(0, 13),
    "Teenager": range(13, 20),
    "Adult": range(20, 60),
    "Senior Citizen": range(60, 150)
}

for group, ages in groups.items():
    if age in ages:
        print("Predicted Age Group:", group)
        break
input("\nPress Enter to exit...")