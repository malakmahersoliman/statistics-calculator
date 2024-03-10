import statistics
import math

# Collect user input for the dataset
data = []
while True:
    try:
        num_points = int(input("Enter the number of data points: "))
        if num_points < 2:
            print("Please enter at least two data points.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(num_points):
    while True:
        try:
            data_point = float(input(f"Enter data point {i + 1}: "))
            data.append(data_point)
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

# Calculate the range
data_range = max(data) - min(data)

# Calculate the total frequency
total_frequency = len(data)

# Calculate the number of classes using the formula
num_classes = 1 + int(3.322 * math.log(total_frequency))

# Calculate the class width
class_width = data_range / num_classes

print(f"Dataset Range: {data_range:.2f}")
print(f"Total Frequency: {total_frequency}")
print(f"Number of Classes: {num_classes}")
print(f"Class Width: {class_width:.2f}")
