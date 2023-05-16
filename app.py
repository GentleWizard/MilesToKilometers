import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    try:
        mile_input = entry_int.get()
        km_output = mile_input * 1.61
        print(km_output)
        output_string.set(km_output)
    except:
        print('Error: Not a number')

# window
window = ttk.Window(themename='journal')
window.title("Miles to Kilometers")
window.geometry("300x150")

# title
title_label = ttk.Label(window, text="Miles to Kilometers", font=("Calibri", 20))
title_label.pack()

# input field
input_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, width=10, textvariable=entry_int)
button = ttk.Button(input_frame, text="Convert", command=convert)
entry.pack(side='left')
button.pack(side='left')
input_frame.pack(pady=10)


# output
output_string = tk.StringVar()
output_label = ttk.Label(
    window,
    text="output",
    font=("Calibri, 20"),
    textvariable=output_string)
output_label.pack()


# run
window.mainloop()