import matplotlib.pyplot as plt

# Create a list of data for the table
data = [
    ('1', 'Comment 1', '10:00 AM', '11:00 AM'),
    ('2', 'Comment 2', '11:30 AM', '12:30 PM'),
    ('3', 'Comment 3', '1:00 PM', '2:00 PM'),
    # Add more data here if needed
]

# Data for the pie chart
hold_numbers = [item[0] for item in data]
start_times = [item[2] for item in data]
end_times = [item[3] for item in data]

# Create the pie chart
plt.pie(end_times, labels=hold_numbers, autopct='%1.1f%%')

# Set the title of the pie chart
plt.title('Hold Numbers Distribution')

# Display the pie chart
plt.show()