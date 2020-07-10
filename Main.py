import tkinter
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile 

top = Tk() 
top.geometry('800x480')
top.title("Azimuth GUI")
top.resizable(width = False, height = False)
statusbar = tkinter.Label(top, text="Welcome Sir,",relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

LeftSideBar=tkinter.Frame(top,borderwidth=3,width=140,height=480,bg='#cfcfcf')
LeftSideBar.pack(side='left',fill='y')

RightSideBar=tkinter.Frame(top,borderwidth=3,width=140,height=480,bg='#cfcfcf')
RightSideBar.pack(side='right',fill='y')
#fileTitle = tkinter.Label(LeftSideBar,text="Select File",width=30)
#fileTitle.pack(side='top',fill='x')

def about():
     messagebox.showinfo('Help', 'Created By Hrushi.')

def quit():
    top.destroy()

def open():
     files = [('JPG (.jpg)', '*.jpg'), 
             ('PNG (.png)', '*.png'),
             ('TIFF (.tiff)', '*.tiff')]
     
     x = filedialog.askopenfilename(filetypes = files, defaultextension = files)
	#img = Image.open(x) 
	#img = img.resize((400, 240), Image.ANTIALIAS) 
	#img = ImageTk.PhotoImage(img) 
	#panel = Label(top, image = img) 
	#panel.image = img 
	#panel.place(x=80)
	
def save(): 
    files = [('JPG (.jpg)', '*.jpg'), 
             ('PNG (.png)', '*.png'),
             ('TIFF (.tiff)', '*.tiff')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)

def filter():
    os.system('denoise.py')

def filter1():
    os.system('kmean.py')

def filter2():
    os.system('ccl.py')
    
#Buttons
Filter = tkinter.Button(LeftSideBar,text="Filter",bg="purple",fg="white",width=8,height=1,font=("Arial Bold", 10),command=filter)
Filter.pack()
Filter.place(x=15,y=5)

Discrimination = tkinter.Button(LeftSideBar,text="Discrimination",bg="purple",fg="white",width=11,height=1,font=("Arial Bold", 10),command=filter1)
Discrimination.pack()
Discrimination.place(x=15,y=35)

CCL = tkinter.Button(LeftSideBar,text="CCL",bg="purple",fg="white",width=8,height=1,font=("Arial Bold", 10),command=filter2)
CCL.pack()
CCL.place(x=15,y=65)

#start = tkinter.Button(LeftSideBar,text="Start",bg="purple",fg="white",width=8,height=1,font=("Arial Bold", 10))
#start.pack()
#start.place(x=15,y=10)

Map = tkinter.Button(LeftSideBar,text="Map",bg="purple",fg="white",width=8,height=1,font=("Arial Bold", 10))
Map.pack()
Map.place(x=15,y=95)

view = tkinter.Button(LeftSideBar,text="View",bg="purple",fg="white",width=8,height=1,font=("Arial Bold", 10))
view.pack()
view.place(x=15,y=125)

#Radio Button1
v1 = tkinter.IntVar()
R1 = Radiobutton(LeftSideBar, text="Land",variable=v1,value=1,font=("Arial Bold", 10),bg='#cfcfcf')
R1.pack()
R1.place(x=35,y=155)
R2 = Radiobutton(LeftSideBar, text="Ocean",variable=v1,value=2,font=("Arial Bold", 10),bg='#cfcfcf')
R2.pack()
R2.place(x=35,y=185)

monitor = tkinter.Button(RightSideBar,text="Monitor",bg="purple",fg="white",width=8,height=1,font=("Arial Bold", 10))
monitor.pack(side=LEFT)
monitor.place(x=10,y=10)

#Radio Button2
v2 = tkinter.IntVar()
R3 = Radiobutton(RightSideBar, text="PlotShip",variable=v2,value=1,font=("Arial Bold", 10),bg='#cfcfcf')
R3.place(x=30,y=40)
R4 = Radiobutton(RightSideBar, text="PlotGraph",variable=v2,value=2,font=("Arial Bold", 10),bg='#cfcfcf')
R4.place(x=30,y=70)


#middle=tkinter.Frame(top,borderwidth=3,width=140,height=480,bg='#cfcfcf')
#middle.pack(side='left',fill='y')

# MiddleFrame
SliderFilter=tkinter.Frame(top)
SliderFilter.pack(side='top',fill='x')
MiddleSideBar=tkinter.Frame(top,borderwidth=3,width=520,height=480,bg="#5555ea")
MiddleSideBar.pack(side='left',fill='y')
#MiddleTable = tkinter.Frame(MiddleSideBar,relief='flat',width=520,height=480)
#MiddleTable.pack(side='left',fill='y')
#MiddleScroll=tkinter.Scrollbar(MiddleSideBar)
#MiddleScroll.pack(side='right',fill='y')


#Menu 
menubar = Menu(top)  
file = Menu(menubar, tearoff=0)    
file.add_command(label="Open",command=open,font=("Arial Bold", 10))
#file.add_command(label="Export",command=save)

file.add_separator()    
file.add_command(label="Exit", command=quit,font=("Arial Bold", 10))

menubar.add_cascade(label="File", menu=file,font=("Arial Bold", 10))  
edit = Menu(menubar, tearoff=0)   
menubar.add_cascade(label="Help", menu=help,command=about)  
      
top.config(menu=menubar)
top.mainloop()  
