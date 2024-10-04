import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Widgets with TKINTER")
window.geometry("400x800")

my_label = ttk.Label(window, text="Hello World!", font=("Arial", 24))
my_label2 = ttk.Label(window, text="Hello World!", font=("Arial", 24))

my_label.pack(pady=10)
my_label2.pack(pady=20)

my_label.config(anchor="center")
my_label["text"] = "New Text"
my_label.config(text="New Text2")

# Buttons
def button_clicked():
    print("Button was clicked!")
    my_label.config(text="Button was clicked!")
    my_label2.config(text=user_input.get())

button = ttk.Button(window, text="Click Me!", command=button_clicked)
button.pack(pady=10)

# Entry
user_input = ttk.Entry(window, width=30)
user_input.pack(pady=10)

# Text
text = tk.Text(height=5, width=30)
text.focus()
text.insert("1.0", "Example of multi-line text entry.")
print(text.get("1.0", "end"))
text.pack(pady=10)

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = ttk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack(pady=10)

# Scale
def scale_used(value):
    print(value)

scale = ttk.Scale(from_=0, to=100, command=scale_used)
scale.pack(pady=10)

# Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = tk.BooleanVar()
checkbutton = ttk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack(pady=10)

# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = tk.IntVar()
radiobutton1 = ttk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = ttk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack(pady=10)
radiobutton2.pack(pady=10)

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack(pady=10)

window.mainloop()
