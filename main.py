from tkinter import *
import tkinter.messagebox
import customtkinter

    
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    """Main app class"""

    #screen config
    WIDTH = 560
    HEIGHT = 525
    
    def __init__(self):
        super().__init__()  
        
        #configure window
        self.title("Calculator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.grid_columnconfigure(0, weight=1)
        
        #input
        self.entry = customtkinter.CTkEntry(self, height=60, width=560, justify=RIGHT, placeholder_text='by kuriimu01',
                    font=customtkinter.CTkFont(family='monospace', size=40))
        self.entry.grid(row=0, pady=10, columnspan=4, sticky="nsew")
        
        #create buttons frame
        self.bframe = customtkinter.CTkFrame(self,  width=560, corner_radius=0)
        self.bframe.grid(row=1, pady=10, column=1, rowspan=4, sticky="nsew")
 
        #buttons
        self.b1 = customtkinter.CTkButton(self.bframe, text='%', height=60).grid(row=1, column=0)
        self.b2 = customtkinter.CTkButton(self.bframe, text='CE', height=60).grid(row=1, column=1)
        self.b3 = customtkinter.CTkButton(self.bframe, text='C', height=60).grid(row=1, column=2)
        self.b4 = customtkinter.CTkButton(self.bframe, text='<', height=60).grid(row=1, column=3)
        self.b5 = customtkinter.CTkButton(self.bframe, text='1/x', height=60).grid(row=2, column=0)
        self.b6 = customtkinter.CTkButton(self.bframe, text='x²', height=60).grid(row=2, column=1)
        self.b7 = customtkinter.CTkButton(self.bframe, text='√x', height=60).grid(row=2, column=2)
        self.b8 = customtkinter.CTkButton(self.bframe, text='÷', height=60).grid(row=2, column=3)
        self.b9 = customtkinter.CTkButton(self.bframe, text='7', height=60, command=lambda : App.add_num(7)).grid(row=3, column=0)
        self.b10 = customtkinter.CTkButton(self.bframe, text='8', height=60, command=lambda : App.add_num(8)).grid(row=3, column=1)
        self.b11 = customtkinter.CTkButton(self.bframe, text='9', height=60, command=lambda : App.add_num(9)).grid(row=3, column=2)
        self.b12 = customtkinter.CTkButton(self.bframe, text='×', height=60).grid(row=3, column=3)
        self.b13 = customtkinter.CTkButton(self.bframe, text='4', height=60, command=lambda : App.add_num(4)).grid(row=4, column=0)
        self.b14 = customtkinter.CTkButton(self.bframe, text='5', height=60, command=lambda : App.add_num(5)).grid(row=4, column=1)
        self.b15 = customtkinter.CTkButton(self.bframe, text='6', height=60, command=lambda : App.add_num(6)).grid(row=4, column=2)
        self.b16 = customtkinter.CTkButton(self.bframe, text='-', height=60).grid(row=4, column=3)
        self.b17 = customtkinter.CTkButton(self.bframe, text='1', height=60, command=lambda : App.add_num(1)).grid(row=5, column=0)
        self.b18 = customtkinter.CTkButton(self.bframe, text='2', height=60, command=lambda : App.add_num(2)).grid(row=5, column=1)
        self.b19 = customtkinter.CTkButton(self.bframe, text='3', height=60, command=lambda : App.add_num(3)).grid(row=5, column=2)
        self.b20 = customtkinter.CTkButton(self.bframe, text='+', height=60).grid(row=5, column=3)
        self.b21 = customtkinter.CTkButton(self.bframe, text='+/-', height=60).grid(row=6, column=0)
        self.b22 = customtkinter.CTkButton(self.bframe, text='0', height=60, command=lambda : App.add_num(0)).grid(row=6, column=1)
        self.b23 = customtkinter.CTkButton(self.bframe, text=',', height=60).grid(row=6, column=2)
        self.b24 = customtkinter.CTkButton(self.bframe, text='=', height=60).grid(row=6, column=3)
                   
        #change appearence 
        self.opframe = customtkinter.CTkFrame(self,  width=560, corner_radius=0)
        self.opframe.grid(row=7, columnspan=4, sticky="nsew")
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.opframe, height=60, values=["Light", "Dark", "System"],
                    command=self.change_appearance_mode_event).grid(row=7, columnspan=4, sticky="nsew")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def add_num(self, num):
         self.entry.insert(0, num)
        
if __name__=='__main__':
    app = App()
    app.mainloop()