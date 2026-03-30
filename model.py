# model.py
import csv

# Simple Linear Regression implementation
class LinearRegressionModel:
    def __init__(self):
        self.m = 0  # slope
        self.b = 0  # intercept

    def train(self, x, y):
        n = len(x)

        x_mean = sum(x) / n
        y_mean = sum(y) / n

        numerator = 0
        denominator = 0

        for i in range(n):
            numerator += (x[i] - x_mean) * (y[i] - y_mean)
            denominator += (x[i] - x_mean) ** 2

        self.m = numerator / denominator
        self.b = y_mean - self.m * x_mean

    def predict(self, x):
        return self.m * x + self.b


# Load student data from CSV
def load_data(file_path):
    study_hours = []
    marks = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            study_hours.append(float(row['study_hours']))
            marks.append(float(row['marks']))

    return study_hours, marks
