from tkinter import *
from tkinter import ttk
import statistics
import matplotlib.pyplot as  plt
import pandas as pd
import numpy as np
import math

root = Tk()
root.title("statistics project")


def tow_line_chart():  # new window definition
    x1 = StringVar()
    y1 = StringVar()
    x2 = StringVar()
    y2 = StringVar()

    def calculate():
        try:
            X1 = x1.get().split(',')
            Y1 = y1.get().split(',')
            X2 = x2.get().split(',')
            Y2 = y2.get().split(',')
            X1 = list(map(int, X1))
            Y1 = list(map(int, Y1))
            X2 = list(map(int, X2))
            Y2 = list(map(int, Y2))
            plt.plot(X1, Y1, 'ro')
            plt.plot(X2, Y2, 'b--')
            plt.axes([0, 15, 0, 15])
            plt.show()
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter X1 axis Values Seperated By ',' ").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x1).grid(column=2, row=1, sticky=(W, E))
    display = Label(newwin, text="Enter X2 axis Values Seperated By ',' ").grid(column=1, row=4, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=x2).grid(column=2, row=4, sticky=(W, E))
    display = Label(newwin, text="Enter Y1 axis Values Seperated By ',' ").grid(column=1, row=7, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=y1).grid(column=2, row=7, sticky=(W, E))
    display = Label(newwin, text="Enter Y2 axis Values Seperated By ',' ").grid(column=1, row=10, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=y2).grid(column=2, row=10, sticky=(W, E))
    ttk.Button(newwin, text="two line chart ", command=calculate).grid(column=5, row=10,
                                                                                               sticky=W)


def line_chart():  # new window definition
    x = StringVar()
    y = StringVar()

    def calculate():
        try:
            X = x.get().split(',')
            Y = y.get().split(',')
            X = list(map(int, X))
            Y = list(map(int, Y))
            plt.plot(X, Y, 'g-')
            plt.title("line chart")
            plt.xlabel("x label")
            plt.ylabel("y label")
            plt.axes([0, 5, 0, 10])
            plt.show()
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter X axis Values Seperated By ',' ").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x).grid(column=2, row=1, sticky=(W, E))
    display = Label(newwin, text="Enter Y axis Values Seperated By ',' ").grid(column=1, row=4, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=y).grid(column=2, row=4, sticky=(W, E))
    ttk.Button(newwin, text="line chart", command=calculate).grid(column=5, row=4, sticky=W)


def bar_chart():  # new window definition
    x = StringVar()
    y = StringVar()

    def calculate():
        try:
            X = x.get().split(',')
            Y = y.get().split(',')
            X = list(map(int, X))
            Y = list(map(int, Y))
            plt.bar(X, Y)
            plt.show()
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter X axis Values Seperated By ',' ").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x).grid(column=2, row=1, sticky=(W, E))
    display = Label(newwin, text="Enter Y axis Values Seperated By ',' ").grid(column=1, row=4, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=y).grid(column=2, row=4, sticky=(W, E))
    ttk.Button(newwin, text="bar chart", command=calculate).grid(column=5, row=4, sticky=W)


def pie_chart():  # new window definition
    x1 = StringVar()
    x2 = StringVar()

    def calculate():
        try:
            m = x2.get().split(',')
            val = list(map(int, m))
            lab = x1.get().split(',')
            plt.pie(val, labels=lab, autopct='%1.1f%%', shadow=True, startangle=140)
            plt.legend(loc='best')
            plt.show()
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter Strings Values Seperated By ',' ").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x1).grid(column=2, row=1, sticky=(W, E))
    display = Label(newwin, text="Enter Values Values Seperated By ',' ").grid(column=1, row=4, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=x2).grid(column=2, row=4, sticky=(W, E))
    ttk.Button(newwin, text="pie chart", command=calculate).grid(column=5, row=10, sticky=W)


def histogram():  # new window definition
    x1 = StringVar()
    x2 = StringVar()

    def calculate():
        try:
            print("Enter")
            m = x2.get()
            val = list(map(int, m))
            num_bins = val[0]
            lab = x1.get().split(',')
            histval = list(map(int, lab))
            plt.hist(histval, num_bins, facecolor='blue', alpha=0.5)
            plt.show()
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter Values Values Seperated By ',' ").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x1).grid(column=2, row=1, sticky=(W, E))
    display = Label(newwin, text="Enter Number of bins(range)").grid(column=1, row=4, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=x2).grid(column=2, row=4, sticky=(W, E))
    ttk.Button(newwin, text="histogram", command=calculate).grid(column=5, row=10, sticky=W)


def boxplot():  # new window definition
    x1 = StringVar()

    def calculate():
        try:
            print("Enter")
            lab = x1.get().split(',')
            boxval = list(map(int, lab))
            df = pd.DataFrame(boxval)
            df.plot.box(grid='True')
            plt.show()
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter Values Seperated By ',' ").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x1).grid(column=2, row=1, sticky=(W, E))
    ttk.Button(newwin, text="boxplot", command=calculate).grid(column=5, row=10, sticky=W)


def Fun():  # new window definition
    x1 = StringVar()
    meter = StringVar()

    def Standerd_Diviation():
        try:
            lab = x1.get().split(',')
            li = list(map(int, lab))
            meter.set(statistics.stdev(li));
        except ValueError:
            pass

    def Variance():
        try:
            lab = x1.get().split(',')
            li = list(map(int, lab))
            meter.set(statistics.variance(li));
        except ValueError:
            pass

    def Mean():
        try:
            lab = x1.get().split(',')
            li = list(map(int, lab))
            meter.set(statistics.mean(li));
        except ValueError:
            pass

    def Mode():
        try:
            print("Enter")
            lab = x1.get().split(',')
            li = list(map(int, lab))
            meter.set(statistics.mode(li));
        except ValueError:
            pass

    def Median():
        try:
            lab = x1.get().split(',')
            li = list(map(int, lab))
            meter.set(statistics.median(li));
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter Values").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x1).grid(column=2, row=1, sticky=(W, E))
    ttk.Button(newwin, text="Mean", command=Mean).grid(column=1, row=10, sticky=W)
    ttk.Button(newwin, text="Median", command=Median).grid(column=2, row=10, sticky=W)
    ttk.Button(newwin, text="Mode", command=Mode).grid(column=3, row=10, sticky=W)
    ttk.Button(newwin, text="Standerd Diviation", command=Standerd_Diviation).grid(column=4, row=10, sticky=W)
    ttk.Button(newwin, text="Variance", command=Variance).grid(column=5, row=10, sticky=W)
    ttk.Label(newwin, text="Value=> ").grid(column=1, row=15, sticky=(W, E))
    ttk.Label(newwin, textvariable=meter).grid(column=2, row=15, sticky=(W, E))


def scater_plot():  # new window definition
    x1 = StringVar()
    x2 = StringVar()
    meter = StringVar()
    Comm = StringVar()

    def Show():
        try:
            print("Enter")
            m = x1.get().split(',')
            sc1 = list(map(int, m))
            lab = x2.get().split(',')
            sc2 = list(map(int, lab))
            plt.scatter(sc1, sc2)
            plt.show()
        except ValueError:
            pass

    def calculate():
        try:
            X = x1.get().split(',')
            Y = x2.get().split(',')
            X = list(map(int, X))
            Y = list(map(int, Y))
            SumX = 0
            SumY = 0
            SumXSquare = 0
            SumYSquare = 0
            SumXY = 0
            Result = 0
            if (len(X) == len(Y)):
                for i in range(0, len(X)):
                    SumX += X[i]
                    SumY += Y[i]
                    SumXSquare += X[i] * X[i]
                    SumYSquare += Y[i] * Y[i]
                    SumXY += Y[i] * X[i]
                Result = ((len(X) * SumXY) - (SumX * SumY)) / math.sqrt(
                    (((len(X) * SumXSquare) - (SumX * SumX)) * ((len(X) * SumYSquare) - (SumY * SumY))))
                print(Result)
                meter.set(Result)
                if 0.9 < Result <= 1:
                    Comm.set("  Coumment: Positive Perfect Corolation")
                elif 0.7 <= Result < 0.9:
                    Comm.set("  Coumment: Positive Strong Corolation")
                elif (0.4 <= Result < 0.6):
                    Comm.set("  Coumment: Positive Moddratd Corolation")
                elif (0 <= Result < 0.4):
                    Comm.set("  Coumment: Positive Week Corolation")
                elif -0.9 > Result >= -1:
                    Comm.set("  Coumment: Negative Perfect Corolation")
                elif -0.7 >= Result > -0.9:
                    Comm.set("  Coumment: Negative Strong Corolation")
                elif (-0.4 >= Result > -0.6):
                    Comm.set("  Coumment: Negative Moddratd Corolation")
                elif (0 >= Result > -0.4):
                    Comm.set("  Coumment: Negative Week Corolation")
        except ValueError:
            pass

    newwin = Toplevel(root)
    display = Label(newwin, text="Enter Scater 1").grid(column=1, row=1, sticky=(W, E))
    feet_entryX = ttk.Entry(newwin, width=20, textvariable=x1).grid(column=2, row=1, sticky=(W, E))
    display = Label(newwin, text="Enter Scater 2").grid(column=1, row=4, sticky=(W, E))
    feet_entryY = ttk.Entry(newwin, width=20, textvariable=x2).grid(column=2, row=4, sticky=(W, E))
    ttk.Button(newwin, text="Correlation", command=calculate).grid(column=5, row=10, sticky=W)
    ttk.Button(newwin, text="Figure", command=Show).grid(column=6, row=10, sticky=W)
    ttk.Label(newwin, text="Value=> ").grid(column=1, row=15, sticky=(W, E))
    ttk.Label(newwin, textvariable=meter).grid(column=1, row=15, sticky=(W, E))
    ttk.Label(newwin, textvariable=Comm).grid(column=2, row=15, sticky=(W, E))


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Please when Enter Any Values Or strings Enter it in This Form "'1,2,3,4,5,6,7,8,9'"").grid(
    column=4, row=0, sticky=(W, E))
ttk.Button(mainframe, text="line chart", command=line_chart).grid(column=0, row=1, sticky=W)
ttk.Button(mainframe, text="tow line chart", command=tow_line_chart).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="bar chart", command=bar_chart).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="pie chart", command=pie_chart).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="histogram", command=histogram).grid(column=5, row=1, sticky=W)
ttk.Button(mainframe, text="boxplot", command=boxplot).grid(column=7, row=1, sticky=W)
ttk.Button(mainframe, text="mean mode median standard diviation", command=Fun).grid(column=6, row=1, sticky=W)
ttk.Button(mainframe, text="Corrolation", command=scater_plot).grid(column=9, row=1, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
