import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk#agg i seperated those two becuase i could not find that class in the backend_tkagg file
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk#css for tkinter
import urllib
import json
import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")#change the style of the graph addes lines to the graph Options are ("dark_background", "grayscale","ggplot")
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)#111 means on chart

def animate(i):#creates the function to pull data from a chart and allows the graph tp update

class FlagShipApp(tk.Tk):
    #adding the bass page
    def __init__(self,*args,**kwargs):#initializes whatever is inside this metthod. Starting method
        tk.Tk.__init__(self,*args,**kwargs)

        tk.Tk.iconbitmap(self , default=r"C:\Users\micha\AppData\Local\Programs\Python\Python37\Scripts\icon.ico")
        #The above adds an icon. you have to define the path of the picture
        tk.Tk.wm_title(self, "Flag Ship")#adds the title

        container = tk.Frame(self)#frame is the window

        container.pack(side="top",fill="both", expand = True)

        container.grid_rowconfigure(0,weight=1)#weight is the priority
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage,PageOne,PageTwo,Flagship_Page):#tuple

            frame = F(container,self)#we have to define start page later

            self.frames[F] = frame

            frame.grid(row=0, column=0,sticky="nsew")#degenerate columns do not show but will show as you fill them
            #--nsew is north south east west and sticky is just which side it sticks to

        self.show_frame(StartPage)#because we are initializing we pull the start StartPage

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):#This is the actual page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="""ALPHA trading application
        use at your own risk""", font = LARGE_FONT)#Seperates the lines
        label.pack(pady=10,padx=10)
        #using ttk rather than tk infront of the button changes the look of the button
        button1 = ttk.Button(self,text="Agree",command=lambda: controller.show_frame(Flagship_Page))
        button1.pack()

        button2 = ttk.Button(self,text="Disagree",command=quit)
        button2.pack()

class PageOne(tk.Frame):#Actuall page one

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page One", font = LARGE_FONT)#predefined font
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Visit Home Page",command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self,text="Visit Page Two",command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self,text="Visit Graph ",command=lambda: controller.show_frame(Flagship_Page))
        button3.pack()

class PageTwo(tk.Frame):#Actuall page two

    def __init__(self,parent,controller):#only thing neccesary to add page, Then add to turple above

        tk.Frame.__init__(self,parent)#only thing neccesary to add page, Then add to turple above

        label = tk.Label(self,text="Page Two", font = LARGE_FONT)#predefined font
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Visit Page One",command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self,text="Visit Home Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()

        button3 = ttk.Button(self,text="Visit Graph ",command=lambda: controller.show_frame(Flagship_Page))
        button3.pack()

class Flagship_Page(tk.Frame):#Actuall page three

    def __init__(self,parent,controller):#only thing neccesary to add page, Then add to turple above

        tk.Frame.__init__(self,parent)#only thing neccesary to add page, Then add to turple above

        label = tk.Label(self,text="Graph Page", font = LARGE_FONT)#predefined font
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Home Page",command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f,self)
        plt.show()#changed this check video 6 if there are issues later with the graph
        canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH, expand = True)

app = FlagShipApp()
ani = animation.FuncAnimation(f,animate, interval=1000)#(figure,which function you want to run,how often you want to run it in miliseconds)
app.mainloop()
