import tkinter as tk
from tkinter import Canvas, ttk

# Window settings
window = tk.Tk()
window.title("test")
window.configure(background="#D3DCED")

# Title label
title_label = tk.Label(window, text="Select Biometrics to Display",font=("ariel",20),background="#D3DCED")
title_label.grid(row=0,column=2, columnspan=2)

# Boolean values 
bool_1 = tk.BooleanVar()
bool_2 = tk.BooleanVar()
bool_3 = tk.BooleanVar()
bool_4 = tk.BooleanVar()
bool_5 = tk.BooleanVar()
bool_6 = tk.BooleanVar()

# Boolean check boxes
boolBox_1 = tk.Checkbutton(window, text="Bool 1", variable=bool_1, width=30, height=3,background="#D3DCED")
boolBox_2 = tk.Checkbutton(window, text="Bool 2", variable=bool_2, width=30, height=3,background="#D3DCED")
boolBox_3 = tk.Checkbutton(window, text="Bool 3", variable=bool_3, width=30, height=3,background="#D3DCED")
boolBox_4 = tk.Checkbutton(window, text="Bool 4", variable=bool_4, width=30, height=3,background="#D3DCED")
boolBox_5 = tk.Checkbutton(window, text="Bool 5", variable=bool_5, width=30, height=3,background="#D3DCED")
boolBox_6 = tk.Checkbutton(window, text="Bool 6", variable=bool_6, width=30, height=3,background="#D3DCED")

# Check box grid allignment 
boolBox_1.grid(row=1,column=0)
boolBox_2.grid(row=1,column=1)            
boolBox_3.grid(row=2,column=0)            
boolBox_4.grid(row=2,column=1)            
boolBox_5.grid(row=3,column=0)            
boolBox_6.grid(row=3,column=1) 

# Radio Variable
radio_var = tk.StringVar()

# Radiobuttons
radio_button1 = tk.Radiobutton(window, text="UTC", variable=radio_var, value="UTC")
radio_button1.grid(row=1,column=4)

radio_button2 = tk.Radiobutton(window, text="LOCAL TIME", variable=radio_var, value="OTHER TIME")
radio_button2.grid(row=1,column=5)

# Radiobutton label
radio_label = tk.Label(window, text="Select Time Interval",font=("ariel",10),background="#D3DCED")
radio_label.grid(row=1,column=3, padx=10)

# Combobox

starthr_box = ttk.Combobox(window, values=["{:02d}".format(h) for h in range(24)], background="#B4C9D6")
starthr_box.grid(row=2,column=4)
startmin_box = ttk.Combobox(window, values=["{:02d}".format(m) for m in range(0,60,10)])
startmin_box.grid(row=2,column=5)

endhr_box = ttk.Combobox(window, values=["{:02d}".format(h) for h in range(24)],background="#B4C9D6")
endhr_box.grid(row=3,column=4)
endmin_box = ttk.Combobox(window, values=["{:02d}".format(m) for m in range(0,60,10)])
endmin_box.grid(row=3,column=5)



# Combobox labels

combo1_label = tk.Label(window, text="Select Start Time",font=("ariel",10),background="#D3DCED")
combo1_label.grid(row=2, column=3, padx=10)
combo2_label = tk.Label(window, text="Select End Time",font=("ariel",10),background="#D3DCED")
combo2_label.grid(row=3, column=3, padx=10)


# Button-click event
def on_button_click():

    print("Button clicked!")

# Button settings    
button = tk.Button(window, text="Create Custom Chart", command=on_button_click)
button.grid(row=7,column=2,columnspan=2)

window.geometry("1250x250")
window.resizable(True, True)

# Start! :3
window.mainloop()
