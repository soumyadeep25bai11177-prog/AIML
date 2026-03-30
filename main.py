# main.py
from model import LinearRegressionModel, load_data
import os

def main():
    print("\n===== Student Performance Predictor =====\n")

    # Correct path to CSV file
    data_path = os.path.join("..", "data", "data.csv")

    # Load data
    try:
        study_hours, marks = load_data(data_path)
    except FileNotFoundError:
        print("Error: data.csv file not found.")
        return

    # Train the model
    model = LinearRegressionModel()
    model.train(study_hours, marks)

    # Take input from user
    try:
        user_hours = float(input("Enter number of study hours: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Predict marks
    predicted_marks = model.predict(user_hours)

    print(f"\nPredicted Marks: {round(predicted_marks, 2)}")

    # Pass/Fail Logic
    if predicted_marks >= 40:
        print("Result: ✅ PASS")
    else:
        print("Result: ❌ FAIL")

    print("\n========================================\n")

if __name__ == "__main__":
    main()
