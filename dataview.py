from tkinter import *
from tkinter.ttk import *

from plotdata import regression_plot
from stats import stats_column

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widget()

    def create_widget(self):
        self.winfo_toplevel().title("Data View")
        self.l1 = Label(self.master, text="File name")
        self.l2 = Label(self.master, text="X Label")
        self.l3 = Label(self.master, text="Y Label")

        self.l1.grid(row=0)
        self.l2.grid(row=1)
        self.l3.grid(row=3)


        self.efname = Entry(self.master, width=40)
        self.eX = Entry(self.master, width=40)
        self.eY = Entry(self.master, width=40)

        self.efname.grid(row=0, column=1, sticky=W)
        self.eX.grid(row=1, column=1, sticky=W)
        self.eY.grid(row=2, column=1, sticky=W)

        self.txtX = Text(self.master, width=30)
        self.txtY = Text(self.master, width=30)

        self.txtX.grid(row=3, column=0, sticky=W)
        self.txtY.grid(row=3, column=1, sticky=W)

        self.style = Style()
        self.style.map('D.TButton',
        foreground=[('pressed', 'red'), ('active', 'green')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )

        self.btn = Button(self.master, text="Show Regression Graph",
        style="D.TButton")
        self.btn["command"] = self.show_graph
        self.btn.grid(row=4, column=0, sticky=W)

        self.stats = Button(self.master, text="Show Stats",
        style="D.TButton")
        self.stats["command"] = self.show_stats
        self.stats.grid(row=4, column=1, sticky=W)

        self.quit = Button(self.master, text="Quite",
        style="D.TButton", command=self.master.destroy
        )
        self.quit.grid(row=4, column=1, sticky=W)

    def show_graph(self):
        regression_plot(self.efname.get(), self.eX.get(), self.eY.get())

    def show_stats(self):
        xstats,ystats = stats_column(self.efname.get(), self.eX.get(), self.eY.get())
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)

root = Tk()
app = Application(master=root)
app.mainloop()