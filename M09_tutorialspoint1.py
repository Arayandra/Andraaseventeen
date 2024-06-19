from tkinter import *
from tkinter import messagebox

# BUTTON
top = Tk()
top.geometry("300x300")

def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
button_frame = Frame(top)
button_frame.pack()
B = Button(button_frame, text ="Hello", command = helloCallBack)
B.pack()

# CHECKBUTTON
checkbutton_frame = Frame(top)
checkbutton_frame.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(checkbutton_frame, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, )
C2 = Checkbutton(checkbutton_frame, text = "Video", variable = CheckVar2, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20)
C1.pack()
C2.pack()

# ENTRY
entry_frame = Frame(top)
entry_frame.pack()

L1 = Label(entry_frame, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(entry_frame, bd =5)
E1.pack(side = RIGHT)

# FRAME
frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton_frame = Frame(top)
blackbutton_frame.pack()

blackbutton = Button(blackbutton_frame, text="Black", fg="black")
blackbutton.pack()

# LABEL
label_frame = Frame(top)
label_frame.pack()

var = StringVar()
label = Label(label_frame, textvariable=var, relief=RAISED )
var.set("Hey!? How are you doing?")
label.pack()

top.mainloop()
