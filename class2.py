
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import Canvas, ttk
from tkinter import messagebox
from tkcalendar import Calendar

import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def exit_program():
    window.destroy()

def update_time():
    global time_start
    time_start = "2020-01-18T" + str(starthr_box.get()) + ":" + str(startmin_box.get()) + ":00Z"
    global time_end
    time_end = "2020-01-18T" + str(endhr_box.get()) + ":" + str(endmin_box.get()) + ":00Z"

def create_graphs():

    update_time()

    global xaxis

    popup_window = tk.Toplevel()  # Create a new popup window
    popup_window.title("Popup Window")
    popup_window.attributes("-fullscreen", True)
    popup_window.geometry("300x200")  # Set the size of the popup window

    # Create toolbar
    toolbar = tk.Frame(popup_window, bg="gray")
    toolbar.pack(side=tk.TOP, fill=tk.X, expand=True)  # Use fill=tk.X and expand=True

    exit_button = tk.Button(toolbar, text="    X    ", command=exit_program)
    exit_button.pack(side=tk.RIGHT)

    file_path = "C:/Users/owner/Downloads/Dataset (2)/Dataset/20200118/310/summary.csv" #file path specific to YOUR computer
    if file_path:
        columns = []  # List to store each column
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first row (title row)
            for row in reader:
                if not columns:
                    columns = [[] for _ in row]  # Create a list for each column
                for i, value in enumerate(row):
                    columns[i].append(value)

    global startIndex
    global endIndex

    try:
        startIndex = columns[0].index(time_start)
        print(f"Value found at index {startIndex}")
    except ValueError:
        print("Value not found in the list")

    try:
        endIndex = columns[0].index(time_end)
        print(f"Value found at index {endIndex}")
    except ValueError:
        print("Value not found in the list")

    timelist = columns[0]

    # Truncate the list
    truncated_list = slice(startIndex, endIndex)
    xaxis = timelist[truncated_list]

    class GraphColumn:
        def __init__(self, title, columnNum, display):
            self.title = title
            self.display = display
            self.columnData = columns[columnNum]

    acc = GraphColumn("Magntiude of Acceleration", 3, bool_1.get())
    eda = GraphColumn("Average EDA", 4, bool_2.get())
    temp = GraphColumn("Average Temperature", 5, bool_3.get())
    move = GraphColumn("Movement", 6, bool_4.get())
    step = GraphColumn("Step Count", 7, bool_5.get())
    rest = GraphColumn("Rest Interval", 8, bool_6.get())

    global columnArray
    columnArray = [acc, eda, temp, move, step, rest]

    y = 4

    # Create a figure and four subplots
    fig = Figure(figsize=(10, 8))
    fig.subplots_adjust(hspace=0.5)  # Adjust spacing between subplots
    
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax6 = fig.add_subplot(236)

    global yaxis
    axes = [ax1, ax2, ax3, ax4, ax5, ax6]
    
    j = 0
    for i in range (len(axes)):
        if columnArray[i].display:
            newlist = columnArray[i].columnData
            yaxis = newlist[slice(startIndex, endIndex)]
            axes[j].plot(xaxis, yaxis)
            axes[j].set_title(columnArray[i].title, fontsize=10, fontweight='bold')

            
                # Customize x-axis tick labels
            x_ticks = len(xaxis) // 5  # Adjust the divisor to control the number of labels
            x_tick_indices = range(0, len(xaxis), x_ticks)
            x_tick_labels = [xaxis[i] for i in x_tick_indices]
            axes[j].set_xticks(x_tick_indices)
            axes[j].set_xticklabels(x_tick_labels, rotation=15)  # Rotate labels if needed

            if(i == 0 or i == 1 or i == 2):
                # Customize y-axis tick labels
                y_ticks = len(yaxis) // 5  # Adjust the divisor to control the number of labels
                y_tick_indices = range(0, len(yaxis), y_ticks)
                y_tick_labels = [yaxis[i] for i in y_tick_indices]
                axes[j].set_yticks(y_tick_indices)
                axes[j].set_yticklabels(y_tick_labels)    

            j = j + 1

    # Create a Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=popup_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add the canvas to the Tkinter window
    canvas.get_tk_widget().pack()

# the main Tkinter window
window = Tk()
window.attributes('-fullscreen', False)  # Set the window to fullscreen
window.configure(background="#D3DCED")

# Title label
title_label = tk.Label(window, text="Select Biometrics to Display",font=("ariel",20),background="#D3DCED")
title_label.grid(row=1,column=4, columnspan=2)

# Boolean values 
bool_1 = tk.BooleanVar()
bool_2 = tk.BooleanVar()
bool_3 = tk.BooleanVar()
bool_4 = tk.BooleanVar()
bool_5 = tk.BooleanVar()
bool_6 = tk.BooleanVar()

# Boolean check boxes
boolBox_1 = tk.Checkbutton(window, text="Magnitude of Acceleration", variable=bool_1, width=30, height=3,background="#D3DCED")
boolBox_2 = tk.Checkbutton(window, text="Average EDA", variable=bool_2, width=30, height=3,background="#D3DCED")
boolBox_3 = tk.Checkbutton(window, text="Average Temperature", variable=bool_3, width=30, height=3,background="#D3DCED")
boolBox_4 = tk.Checkbutton(window, text="Movement", variable=bool_4, width=30, height=3,background="#D3DCED")
boolBox_5 = tk.Checkbutton(window, text="Step Count", variable=bool_5, width=30, height=3,background="#D3DCED")
boolBox_6 = tk.Checkbutton(window, text="Rest Interval", variable=bool_6, width=30, height=3,background="#D3DCED")

# Check box grid alignment 
boolBox_1.grid(row=2,column=0)
boolBox_2.grid(row=2,column=1)            
boolBox_3.grid(row=3,column=0)            
boolBox_4.grid(row=3,column=1)            
boolBox_5.grid(row=4,column=0)            
boolBox_6.grid(row=4,column=1) 

def validate_date_range():
    start_date = cal_start.get_date()
    end_date = cal_end.get_date()
    
    min_date = datetime.strptime("1-17-2020", "%m-%d-%Y").date()
    max_date = datetime.strptime("1-19-2020", "%m-%d-%Y").date()
    
    # Ensure all dates are of datetime.date type
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%m-%d-%Y").date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%m-%d-%Y").date()
    
    if start_date >= min_date and end_date <= max_date and end_date >= start_date:
        messagebox.showinfo("Success", f"Selected range: {start_date} to {end_date}")
    else:
        messagebox.showerror("Error", "Selected range must be within 1-18-2020 to 1-19-2020 and end date should be greater or equal to start date.")


# Create Start Date calendar
label_start = tk.Label(window, text="Start Date:")
label_start.grid(row=2, column=7)
cal_start = Calendar(window, date_pattern='M-d-y')
cal_start.grid(row=3, column=7, padx=10, pady=10)

# Create End Date calendar
label_end = tk.Label(window, text="End Date:")
label_end.grid(row=2, column=9)
cal_end = Calendar(window, date_pattern='M-d-y')
cal_end.grid(row=3, column=9, padx=10, pady=10)

# Create a button to validate the selected range
button_validate = tk.Button(window, text="Validate", command=validate_date_range)
button_validate.grid(row=4, column=8)


# Radio Variable
radio_var = tk.StringVar()

# Radiobuttons
radio_button1 = tk.Radiobutton(window, text="UTC", variable=radio_var, value="UTC")
radio_button1.grid(row=2,column=4)

radio_button2 = tk.Radiobutton(window, text="LOCAL TIME", variable=radio_var, value="OTHER TIME")
radio_button2.grid(row=2,column=5)

# Radiobutton label
radio_label = tk.Label(window, text="Select Time Interval",font=("ariel",10),background="#D3DCED")
radio_label.grid(row=2,column=3, padx=10)

# Combobox
starthr_box = ttk.Combobox(window, values=["{:02d}".format(h) for h in range(24)], background="#B4C9D6")
starthr_box.grid(row=3,column=4)
starthr_box.current(0)
startmin_box = ttk.Combobox(window, values=["{:02d}".format(m) for m in range(0,60)])
startmin_box.grid(row=3,column=5)
startmin_box.current(0)

endhr_box = ttk.Combobox(window, values=["{:02d}".format(h) for h in range(24)],background="#B4C9D6")
endhr_box.grid(row=4,column=4)
endhr_box.current(1)
endmin_box = ttk.Combobox(window, values=["{:02d}".format(m) for m in range(0,60)])
endmin_box.grid(row=4,column=5)
endmin_box.current(0)

starthr_box.bind("<<ComboboxSelected>>", lambda _: update_time())
startmin_box.bind("<<ComboboxSelected>>", lambda _: update_time())
endhr_box.bind("<<ComboboxSelected>>", lambda _: update_time())
endmin_box.bind("<<ComboboxSelected>>", lambda _: update_time())

# Combobox labels
combo1_label = tk.Label(window, text="Select Start Time",font=("ariel",10),background="#D3DCED")
combo1_label.grid(row=3, column=3, padx=10)
combo2_label = tk.Label(window, text="Select End Time",font=("ariel",10),background="#D3DCED")
combo2_label.grid(row=4, column=3, padx=10)

# setting the title
window.title('Health Monitor')

# button that displays the plot
plot_button = Button(master=window,
                     command=create_graphs,
                     height=2,
                     width=10,
                     text="Plot")

# place the button in the main window
plot_button.grid(row=6, column=3, pady=10)

# run the gui
window.mainloop()
    
