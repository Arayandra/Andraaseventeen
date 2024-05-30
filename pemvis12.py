import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser


def draw_shape():
    shape = shape_var.get()
    canvas.delete("all")

    if shape == 'Line':
        try:
            x1 = int(x1_entry.get())
            y1 = int(y1_entry.get())
            x2 = int(x2_entry.get())
            y2 = int(y2_entry.get())
            thickness = int(thickness_entry.get())
            color = color_var.get()
            canvas.create_line(x1, y1, x2, y2, fill=color, width=thickness)
        except ValueError:
            pass

    elif shape == 'Rectangle':
        try:
            x1 = int(x1_entry.get())
            y1 = int(y1_entry.get())
            x2 = int(x2_entry.get())
            y2 = int(y2_entry.get())
            thickness = int(thickness_entry.get())
            outline_color = color_var.get()
            fill_color = fill_color_var.get()
            canvas.create_rectangle(x1, y1, x2, y2, outline=outline_color, width=thickness, fill=fill_color)
        except ValueError:
            pass

    elif shape == 'Circle':
        try:
            x = int(x1_entry.get())
            y = int(y1_entry.get())
            radius = int(radius_entry.get())
            thickness = int(thickness_entry.get())
            outline_color = color_var.get()
            fill_color = fill_color_var.get()
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=outline_color, width=thickness,
                               fill=fill_color)
        except ValueError:
            pass


def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")[1]
    color_var.set(color_code)


def choose_fill_color():
    color_code = colorchooser.askcolor(title="Choose fill color")[1]
    fill_color_var.set(color_code)


root = tk.Tk()
root.title("Shape Drawer")

# Canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.grid(row=0, column=0, rowspan=10)

# Shape selection
shape_var = tk.StringVar(value="Line")
shapes = ["Line", "Rectangle", "Circle"]
tk.Label(root, text="Choose shape:").grid(row=0, column=1, sticky=tk.W)
shape_menu = ttk.Combobox(root, textvariable=shape_var, values=shapes, state='readonly')
shape_menu.grid(row=0, column=2, sticky=tk.W)

# Coordinates and attributes inputs
tk.Label(root, text="x1:").grid(row=1, column=1, sticky=tk.W)
x1_entry = tk.Entry(root)
x1_entry.grid(row=1, column=2, sticky=tk.W)

tk.Label(root, text="y1:").grid(row=2, column=1, sticky=tk.W)
y1_entry = tk.Entry(root)
y1_entry.grid(row=2, column=2, sticky=tk.W)

tk.Label(root, text="x2:").grid(row=3, column=1, sticky=tk.W)
x2_entry = tk.Entry(root)
x2_entry.grid(row=3, column=2, sticky=tk.W)

tk.Label(root, text="y2:").grid(row=4, column=1, sticky=tk.W)
y2_entry = tk.Entry(root)
y2_entry.grid(row=4, column=2, sticky=tk.W)

tk.Label(root, text="Radius:").grid(row=5, column=1, sticky=tk.W)
radius_entry = tk.Entry(root)
radius_entry.grid(row=5, column=2, sticky=tk.W)

tk.Label(root, text="Thickness:").grid(row=6, column=1, sticky=tk.W)
thickness_entry = tk.Entry(root)
thickness_entry.grid(row=6, column=2, sticky=tk.W)

# Color selection
color_var = tk.StringVar(value="black")
tk.Label(root, text="Line color:").grid(row=7, column=1, sticky=tk.W)
color_button = tk.Button(root, text="Choose color", command=choose_color)
color_button.grid(row=7, column=2, sticky=tk.W)

fill_color_var = tk.StringVar(value="")
tk.Label(root, text="Fill color:").grid(row=8, column=1, sticky=tk.W)
fill_color_button = tk.Button(root, text="Choose fill color", command=choose_fill_color)
fill_color_button.grid(row=8, column=2, sticky=tk.W)

# Draw button
draw_button = tk.Button(root, text="Draw", command=draw_shape)
draw_button.grid(row=9, column=1, columnspan=2)

root.mainloop()
