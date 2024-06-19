import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog, Frame
from tkinter import ttk
from tkinter.messagebox import showinfo


# Fungsi untuk Load Data
def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global df
        df = pd.read_csv(file_path)
        showinfo("Info", "Data loaded successfully!")
        update_combo()
        display_data()


# Fungsi untuk menampilkan data pada tabel
def display_data():
    if df is not None:
        # Clear existing data
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data
        for idx, row in df.iterrows():
            tree.insert("", "end", values=list(row))

        # Update column headings
        tree["columns"] = list(df.columns)
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)


# untuk merangkum data
def summarize_data():
    if df is not None:
        showinfo("Summary Statistics", df.describe().to_string())


# untuk plot data dengan grafik
def plot_data():
    if df is not None:
        column = combo.get()
        plt.figure(figsize=(10, 5))
        df[column].value_counts().plot(kind='bar')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()
def update_combo():
    if df is not None:
        combo['values'] = df.columns.tolist()


# Menu utama
root = Tk()
root.title("DAG Data")

# buat frame
frame = Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# tombol load data
load_button = Button(frame, text="Load Data", command=load_data)
load_button.grid(row=0, pady=10)

# display data
tree = ttk.Treeview(frame, show='headings')
tree.grid(row=1, pady=10)

# tombol summary data
summary_button = Button(frame, text="Show Summary", command=summarize_data)
summary_button.grid(row=2, pady=10)

# combo box untuk select kolom
combo = ttk.Combobox(frame)
combo.grid(row=2, pady=10)

# tombol untuk plot data
plot_button = Button(frame, text="Plot Data", command=plot_data)
plot_button.grid(row=3, pady=10)

# inisialisasi dataframe
df = None

root.mainloop()
