import tkinter as tk
from tkinter import ttk

# Create a list of data for the table
data = [
    ('1', 'Comment 1', '10:00 AM', '11:00 AM'),
    ('2', 'Comment 2', '11:30 AM', '12:30 PM'),
    ('3', 'Comment 3', '1:00 PM', '2:00 PM'),
    # Add more data here if needed
]

# Create the Tkinter window
window = tk.Tk()
window.title('Table Example')

# Create a Treeview widget
tree = ttk.Treeview(window, columns=('Hold #', 'Comment', 'Start time', 'End time'), show='headings')

# Define the columns and their headings
tree.heading('Hold #', text='Hold #')
tree.heading('Comment', text='Comment')
tree.heading('Start time', text='Start time')
tree.heading('End time', text='End time')

# Define the column widths
tree.column('Hold #', width=80, anchor='center')
tree.column('Comment', width=150, anchor='center')
tree.column('Start time', width=100, anchor='center')
tree.column('End time', width=100, anchor='center')

# Insert the data into the table
for item in data:
    tree.insert('', 'end', values=item)

# Add the Treeview widget to the window
tree.pack(fill='both', expand=True)

# Start the Tkinter event loop
window.mainloop()