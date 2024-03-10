import matplotlib.pyplot as plt

def calculate_mean(grouped_data, x_values):
    total_sum = sum(mid_point * frequency for (lower, upper, frequency), mid_point in zip(grouped_data, x_values))
    total_frequency = sum(frequency for lower, upper, frequency in grouped_data)
    return total_sum / total_frequency

def calculate_mode(x_values, y_values):
    mode_index = y_values.index(max(y_values))
    return x_values[mode_index]

def calculate_median(grouped_data, total_frequency, x_values):
    cumulative_frequency = 0
    median_group = ()

    for group_data in grouped_data:
        cumulative_frequency += group_data[2]
        if cumulative_frequency >= total_frequency / 2:
            median_group = group_data  
            break

    return median_group[0] + ((total_frequency / 2 - (cumulative_frequency - group_data[2])) / group_data[2]) * (group_data[1] - group_data[0])

def plot_histogram(grouped_data, x_values, y_values):
   
    bar_width = min(abs(x_values[i + 1] - x_values[i]) for i in range(len(x_values) - 1))  # Calculate the width 
    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, width=bar_width, alpha=0.7)

    # Set title and labels
    plt.title('Histogram for Grouped Data')
    plt.xlabel('Midpoints')
    plt.ylabel('Frequency')

    plt.show()    # Show the plot

# Initialize an empty list to store the grouped data
grouped_data = []
#input 
num_groups = int(input("Enter the number of groups: "))

# Loop to collect data
for group in range(1, num_groups + 1):
    lower_bound = float(input(f"Enter the lower bound of Group {group}: "))
    upper_bound = float(input(f"Enter the upper bound of Group {group}: "))
    frequency = int(input(f"Enter the frequency for Group {group}: "))
    grouped_data.append((lower_bound, upper_bound, frequency))
 
# Display  data
print("\nCollected Grouped Data:")
for group_data in grouped_data:
    print(f"Group: {group_data[0]} - {group_data[1]}, Frequency: {group_data[2]}")

x_values = [(group_data[0] + group_data[1]) / 2 for group_data in grouped_data] #midpoint
y_values = [group_data[2] for group_data in grouped_data]
total_frequency = sum(frequency for lower, upper, frequency in grouped_data)

mean_result = calculate_mean(grouped_data, x_values)
mode_result = calculate_mode(x_values, y_values)
median_result = calculate_median(grouped_data, total_frequency, x_values)

print(f"\nMean: {mean_result}")
print(f"Mode: {mode_result}")
print(f"Median: {median_result}")

plot_histogram(grouped_data, x_values, y_values)
