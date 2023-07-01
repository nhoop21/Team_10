# Imports
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog, ttk, Label, Button, Tk, BooleanVar, Checkbutton, Radiobutton, StringVar
import pandas as pd
import csv
import matplotlib.pyplot as plt


# Select file function
def select_file():
    # File dialog box window config
    window = tk.Tk()
    window.withdraw()

    # Open a file dialog box to select the CSV file
    filepath = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    # Close the file dialog box window
    window.destroy()

    # Check if a file was selected
    if filepath:
        return pd.read_csv(filepath), filepath
    else:
        print("No file selected.")
        exit()

# Assign variables 
data, filepath = select_file()


# Time range function
def read_datetime_values_from_csv(filepath):
    local_datetime_values = []
    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            local_datetime_values.append(datetime.strptime(row['Datetime (UTC)'], '%Y-%m-%dT%H:%M:%SZ'))
    return local_datetime_values


# Extract first and last datetime values
datetime_values = read_datetime_values_from_csv(filepath)

first_datetime = datetime_values[0]
last_datetime = datetime_values[-1]

minutes_range = int((last_datetime - first_datetime).total_seconds() / 60) + 1
datetime_range = [first_datetime + timedelta(minutes=x) for x in range(0, minutes_range)]

datetime_strings = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in datetime_range]

# Create Graph Function
def create_graphs():

    # Assign start and end datetimes from selection
    start_datetime = start_datetime_combobox.get()
    end_datetime = end_datetime_combobox.get()

    filtered_data = data[(data['Datetime (UTC)'] >= start_datetime) & (data['Datetime (UTC)'] <= end_datetime)]

    # Extract necessary data for plotting
    x1 = filtered_data['Datetime (UTC)']
    y1 = filtered_data['Acc magnitude avg']
    y2 = filtered_data['Eda avg']
    y3 = filtered_data['Temp avg']
    y4 = filtered_data['Movement intensity']
    y5 = filtered_data['Steps count']
    y6 = filtered_data['Rest']

    # Create the figure and subplots
    fig = plt.figure(figsize=(12, 8))

    plot_index = 1

    # First subplot
    if bool_1.get():
        ax1 = fig.add_subplot(2, 3, plot_index)
        ax1.plot(x1, y1)
        ax1.set_title('Acc Mag Evg')
        plot_index += 1

    # Second subplot
    if bool_2.get():
        ax2 = fig.add_subplot(2, 3, plot_index)
        ax2.plot(x1, y2)
        ax2.set_title('EDA Avg')
        plot_index += 1

    # Third subplot
    if bool_3.get():
        ax3 = fig.add_subplot(2, 3, plot_index)
        ax3.plot(x1, y3)
        ax3.set_title('Temp Avg')
        plot_index += 1

    # Fourth subplot
    if bool_4.get():
        ax4 = fig.add_subplot(2, 3, plot_index)
        ax4.plot(x1, y4)
        ax4.set_title('Movement Intensity')
        plot_index += 1

    # Fifth subplot
    if bool_5.get():
        ax5 = fig.add_subplot(2, 3, plot_index)
        ax5.plot(x1, y5)
        ax5.set_title('Steps Count')
        plot_index += 1

    # Sixth subplot
    if bool_6.get():
        ax6 = fig.add_subplot(2, 3, plot_index)
        ax6.plot(x1, y6)
        ax6.set_title('Rest')
        plot_index += 1

    # Adjust the spacing between subplots
    fig.tight_layout()

    # Display the figure
    plt.show()


# Data selection window config
window = Tk()
window.attributes('-fullscreen', False)
window.configure(background="#D3DCED")
window.title('Health Monitor')

# Title label
title_label = tk.Label(window, text="Select Biometrics to Display",font=("ariel",20),background="#D3DCED")
title_label.grid(row=1,column=1, columnspan=2)

# Comboboxes
label = Label(window, text="Select a Start Datetime:",background="#D3DCED")
label.grid(row=3, column=2)

label = Label(window, text="Select an End Datetime:",background="#D3DCED")
label.grid(row=4, column=2)

start_datetime_combobox = ttk.Combobox(window, values=datetime_strings)
start_datetime_combobox.grid(row=3, column=3, columnspan=2)

end_datetime_combobox = ttk.Combobox(window, values=datetime_strings)
end_datetime_combobox.grid(row=4, column=3, columnspan=2)


# Checkbuttons
bool_1 = tk.BooleanVar()
bool_2 = tk.BooleanVar()
bool_3 = tk.BooleanVar()
bool_4 = tk.BooleanVar()
bool_5 = tk.BooleanVar()
bool_6 = tk.BooleanVar()

boolBox_1 = tk.Checkbutton(window, text="Magnitude of Acceleration", variable=bool_1, width=30, height=3,background="#D3DCED")
boolBox_2 = tk.Checkbutton(window, text="Average EDA", variable=bool_2, width=30, height=3,background="#D3DCED")
boolBox_3 = tk.Checkbutton(window, text="Average Temperature", variable=bool_3, width=30, height=3,background="#D3DCED")
boolBox_4 = tk.Checkbutton(window, text="Movement", variable=bool_4, width=30, height=3,background="#D3DCED")
boolBox_5 = tk.Checkbutton(window, text="Step Count", variable=bool_5, width=30, height=3,background="#D3DCED")
boolBox_6 = tk.Checkbutton(window, text="Rest Interval", variable=bool_6, width=30, height=3,background="#D3DCED")

boolBox_1.grid(row=2,column=0)
boolBox_2.grid(row=2,column=1)            
boolBox_3.grid(row=3,column=0)            
boolBox_4.grid(row=3,column=1)            
boolBox_5.grid(row=4,column=0)            
boolBox_6.grid(row=4,column=1) 


# Radiobuttons
radio_label = tk.Label(window, text="Select Time Interval",font=("ariel",10),background="#D3DCED")
radio_label.grid(row=2,column=2)

radio_var = tk.StringVar(value="UTC")

radio_button1 = tk.Radiobutton(window, text="UTC", variable=radio_var, value="UTC")
radio_button1.grid(row=2,column=3)

radio_button2 = tk.Radiobutton(window, text="LOCAL TIME", variable=radio_var, value="OTHER TIME")
radio_button2.grid(row=2,column=4)


# Plot button
plot_button = Button(master=window,command=create_graphs,height=2,width=10,text="Plot")
plot_button.grid(row=6, column=1, pady=10)


# Execute 
window.mainloop()
    