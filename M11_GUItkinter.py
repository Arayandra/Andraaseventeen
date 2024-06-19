#CREATING GUI USING TKINTER
import tkinter as tk
#Jalankan Code untuk tiap topik bergantian. Bergantian Beri tanda # untu topik yang
#tidak dijalankan

root = tk.Tk()

#============================================================
#-----------------------Latihan-1 : Membuat Widget Dasat------
#============================================================
#WidgetDasarku.mainloop()
#WidgetDasarku.mainloop()

#Latihan-2 : Membuat Canvas
#Kanvasku = tk.Canvas(root, height = 1000, width = 1920)
#Kanvasku.pack()

#Latihan-3: Membuat Canvas
Frameku = tk.Frame(root, bg = 'purple')
Frameku.place(relwidth = 0.8, relheight = 0.8)

#root.mainloop()

#Latihan membuat button di root
#Tombolku = tk.button(root, text = " Tes Tombol ", bg = 'gray', fg ='red')
#Tombolku.pack()

#Latihan membuat button di frame
Tombolku = tk.Button(Frameku, text = " Tes Tombol ", bg = 'gray', fg ='red')
Tombolku.pack()

#Latihan membuat Entry
Entry = tk.Entry(Frameku, bg = 'green')
Entry.pack()

root.mainloop()