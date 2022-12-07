from tkinter import *
import tkinter.messagebox
import customtkinter
import os, sys
  
customtkinter.set_appearance_mode("System")  # "System" (standard), "Dark", "Light"
  # "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    """Main app class"""

    # screen config
    WIDTH = 380
    HEIGHT = 380
    
    def __init__(self):
        super().__init__()  
        
        # configure window
        self.title("Calculator by kuriimu01")
        self.iconbitmap('./img/icon.ico')
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.grid_columnconfigure(0, weight=1)
        
        
        # create main entry
        self.entry = customtkinter.CTkEntry(self, height=60, justify=RIGHT,
                    font=customtkinter.CTkFont(family='monospace', size=40))
        self.entry.grid(row=0, pady=10, columnspan=4, sticky="nsew")
        
        # create buttons frame
        self.bframe = customtkinter.CTkFrame(self, corner_radius=0)
        self.bframe.grid(row=1, pady=10, column=0, rowspan=4, sticky="nsew")
        self.bframe.grid_columnconfigure((0,1,2,3), weight=1)
        self.bframe.grid_rowconfigure(1, weight=1)
        # buttons
        self.b1 = customtkinter.CTkButton(self.bframe, text='%', command=lambda : self.add_num('%'))
        self.b2 = customtkinter.CTkButton(self.bframe, text='CE')
        self.b3 = customtkinter.CTkButton(self.bframe, text='C', command= lambda : self.clear())
        self.b4 = customtkinter.CTkButton(self.bframe, text='<', command= lambda : self.delete_one())
        self.b5 = customtkinter.CTkButton(self.bframe, text='1/x', command= lambda : self.add_opp('1/'))
        self.b6 = customtkinter.CTkButton(self.bframe, text='x²', command=lambda : self.add_num('²'))
        self.b7 = customtkinter.CTkButton(self.bframe, text='√x')
        self.b8 = customtkinter.CTkButton(self.bframe, text='÷', command= lambda : self.add_opp('÷'))
        self.b9 = customtkinter.CTkButton(self.bframe, text='7', command=lambda : self.add_num(7))
        self.b10 = customtkinter.CTkButton(self.bframe, text='8', command=lambda : self.add_num(8))
        self.b11 = customtkinter.CTkButton(self.bframe, text='9', command=lambda : self.add_num(9))
        self.b12 = customtkinter.CTkButton(self.bframe, text='×', command=lambda : self.add_opp('×'))
        self.b13 = customtkinter.CTkButton(self.bframe, text='4', command=lambda : self.add_num(4))
        self.b14 = customtkinter.CTkButton(self.bframe, text='5', command=lambda : self.add_num(5))
        self.b15 = customtkinter.CTkButton(self.bframe, text='6', command=lambda : self.add_num(6))
        self.b16 = customtkinter.CTkButton(self.bframe, text='-', command=lambda : self.add_opp('-'))
        self.b17 = customtkinter.CTkButton(self.bframe, text='1', command=lambda : self.add_num(1))
        self.b18 = customtkinter.CTkButton(self.bframe, text='2', command=lambda : self.add_num(2))
        self.b19 = customtkinter.CTkButton(self.bframe, text='3', command=lambda : self.add_num(3))
        self.b20 = customtkinter.CTkButton(self.bframe, text='+', command=lambda : self.add_opp('+'))
        self.b21 = customtkinter.CTkButton(self.bframe, text='+/-')
        self.b22 = customtkinter.CTkButton(self.bframe, text='0', command=lambda : self.add_num(0))
        self.b23 = customtkinter.CTkButton(self.bframe, text='.', command=lambda : self.add_opp('.'))
        self.b24 = customtkinter.CTkButton(self.bframe, text='=', command= lambda : self.calc())
        
        # add buttons
        btn_list = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8,
                    self.b9, self.b10, self.b11, self.b12, self.b13, self.b14, self.b15, self.b16,
                    self.b17, self.b18, self.b19, self.b20, self.b21, self.b22, self.b23, self.b24,]
        column = 0
        row=1
        for button in btn_list: 
            if column > 3:
                column = 0
                row+=1   
            if row > 6: break
            button.grid(row=row, column=column, pady=2, padx=2, sticky="nsew") 
            column+=1    
    
        # change appearence 
        self.opframe = customtkinter.CTkFrame(self,  width=560, corner_radius=0)
        self.opframe.grid(row=7, column=0, columnspan=4,  sticky="nsew")
        self.opframe.grid_columnconfigure((0,1,2,3), weight=1)
        self.opframe.grid_rowconfigure(7, weight=1)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.opframe, height=60, values=["System", "Dark", "Light"],
                    command=self.change_appearance_mode_event).grid(row=7, columnspan=4, sticky="nsew")
               
        # default values
        self.add_num(0)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # add num to entry
    def add_opp(self, opp):
        entry_text = self.entry.get()
        if entry_text[-1] in '%+-÷×/.':
            entry_text = entry_text[:-1]
        elif '+' in entry_text or '-' in entry_text or '×' in entry_text or '÷' in entry_text or '/' in entry_text:
            self.calc()
            entry_text = self.entry.get()
        if entry_text == '0' and opp=='1/':
            entry_text = entry_text[:-1]
        self.entry.delete(0, customtkinter.END)
        self.entry.insert(0, entry_text+opp)        

    def add_num(self, num):
        entry_text = self.entry.get()
        if entry_text == '0' and type(num)==int:
            self.entry.delete(0, customtkinter.END)
            self.entry.insert(0, num)
        else:
            value = entry_text + str(num)
            self.entry.delete(0, customtkinter.END)
            self.entry.insert(0, value)
    
    # clear entry
    def clear(self):
        self.entry.delete(0, customtkinter.END)
        self.entry.insert(0, 0)
    
    def delete_one(self):
        self.entry.delete(len(self.entry.get())-1, customtkinter.END)
        
    # main calculator func
    def calc(self):
        result=''
        entry_text=''
        for op in self.entry.get():
            if op=='×':
                entry_text+='*'
            elif op=='%':
                entry_text+='/100'
            elif op=='÷':
                entry_text+='/'
            elif op=='²':
                range = 0
                nums=''
                delete_list = []
                for op in entry_text:
                    try:
                        int(op)
                    except:
                        range = entry_text.index(op)
                if range==0:
                    count=0
                    for num in entry_text:
                        nums+=num
                    entry_text = entry_text.replace(nums, "")
                else:
                    count = 0
                    for num in entry_text:
                        if count>range:
                            nums+=num
                        count+=1
                    entry_text = entry_text.replace(nums, "")
                entry_text+= f'pow({nums} ,2)'
            else:
                entry_text+=op
        try:        
            result = eval(entry_text)
            self.entry.delete(0, customtkinter.END)
            self.entry.insert(0, result)
        except ZeroDivisionError:
            self.clear()
            tkinter.messagebox.showerror(title='Error', message='Cannot be divided by zero.')
     
        
if __name__=='__main__':
    app = App()
    app.mainloop()