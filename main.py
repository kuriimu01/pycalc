from tkinter import *
import sys

root = Tk()
root.geometry("390x370")
root.title("Calculator")

#Add input
e = Entry(root, bg='#1C1C1C', width=40, borderwidth=15, fg="white", font=35, ).grid(row=0, columnspan=4, sticky='NSEW')


#Operator buttons
percent = Button(root, text="%", padx=38, pady=15, bg='#D4D4D2').grid(row=1, column=0)
clr_this = Button(root, text="CE", padx=38, pady=15, bg='#D4D4D2').grid(row=1, column=1)
clr_all = Button(root, text="C", padx=38, pady=15, bg='#D4D4D2').grid(row=1, column=2)
inverse = Button(root, text="1/x", padx=35, pady=15, bg='#D4D4D2').grid(row=2, column=0)
sqr = Button(root, text="x²", padx=39, pady=15, bg='#D4D4D2').grid(row=2, column=1)
sqrroot = Button(root, text="√x", padx=37, pady=15, bg='#D4D4D2').grid(row=2, column=2)

#Left sidebar 
clr_left = Button(root, text="<", padx=37, pady=15, fg='white', bg='#FF9500', activebackground='#E68600').grid(row=1, column=3)
div = Button(root, text="÷", padx=37, pady=15, fg='white', bg='#FF9500', activebackground='#E68600').grid(row=2, column=3)
multiple = Button(root, text="×", padx=37, pady=15, fg='white', bg='#FF9500', activebackground='#E68600').grid(row=3, column=3)
minus = Button(root, text="-", padx=37, pady=15, fg='white', bg='#FF9500', activebackground='#E68600').grid(row=4, column=3)
plus = Button(root, text="+", padx=37, pady=15, fg='white', bg='#FF9500', activebackground='#E68600').grid(row=5, column=3)
equals = Button(root, text="=", padx=37, pady=15, fg='white', bg='#FF9500', activebackground='#E68600').grid(row=6, column=3)

#Int buttons
b7 = Button(root, text="7", padx=40, pady=15,fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=3, column=0)
b8 = Button(root, text="8", padx=40, pady=15,fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=3, column=1)
b9 = Button(root, text="9", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=3, column=2)
b4 = Button(root, text="4", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=4, column=0)
b5 = Button(root, text="5", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=4, column=1)
b6 = Button(root, text="6", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=4, column=2)
b1 = Button(root, text="1", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=5, column=0)
b2 = Button(root, text="2", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=5, column=1)
b3 = Button(root, text="3", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=5, column=2)
b1 = Button(root, text="+/-", padx=34, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=6, column=0)
b0 = Button(root, text="0", padx=40, pady=15, fg='white', bg='#505050', 
    activebackground='#5E5E5E', activeforeground='white').grid(row=6, column=1)
bp = Button(root, text=".", padx=40, pady=15, fg='white', bg='#505050',
    activebackground='#5E5E5E', activeforeground='white').grid(row=6, column=2)

root.mainloop()