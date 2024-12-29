
import matplotlib.pyplot as plt

# Data
ages = ['0-10', '11-20', '21-30', '31-40', '41-50', '51+']  # Age groups
population = [500, 600, 800, 700, 650, 400]  # Population for each age group

# Create the bar chart
plt.figure(figsize=(8, 5))  # Set the figure size
plt.bar(ages, population, color='lightblue', edgecolor='black')

# Add labels and title
plt.title('Population Distribution by Age Group', fontsize=16)
plt.xlabel('Age Groups', fontsize=14)
plt.ylabel('Population', fontsize=14)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the bar chart
plt.show()
