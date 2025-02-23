import customtkinter as ctk
from PIL import Image
from view.fonts import *
from pathlib import Path
from tkinter import PhotoImage

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, master, default_gray):
        self.mode = 'dark'
        self.current_theme = 'blue'
        super().__init__(master)
        self.geometry("400x300")
        self.wm_attributes("-topmost", True)
        
        # Get correct icon path
        base_dir = pathlib.Path(__file__).resolve().parent.parent  
        icon_path = base_dir.joinpath('src', 'img', 'app_icon.ico')

        # Delay setting icon to override customtkinter default behavior
        self.after(250, lambda: self.iconbitmap(icon_path))
        
        self.resizable(False, False)
        self.configure(bg='#2b2b2b')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title row
        self.grid_rowconfigure(1, weight=0)  # Mode Switch button (fixed)
        
        # Define paths 
        current_dir = Path(__file__).resolve().parent
        img_path = current_dir.parent.joinpath('src', 'img')
        
        # Title
        self.label = ctk.CTkLabel(self, text="Settings", font=title_font())
        self.label.grid(row = 0, column = 0, pady=(15,10))
        
        # Mode setting
        mode_img = Image.open(
            img_path.joinpath('mode_switch.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_mode = ctk.CTkImage(mode_img, size=(14,14))
        self.change_mode_btn = ctk.CTkButton(self, text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='Switch Mode', font=small_button_font(), image=self.img_mode, command=self.change_mode)
        self.change_mode_btn.grid(row=1, column=0, pady = (10,5), sticky='ns')
              
        
    def change_mode(self):
        if self.mode == 'dark':
            ctk.set_appearance_mode("light")
            self.mode = 'light'
        else:
            ctk.set_appearance_mode('dark')
            self.mode = 'dark' 
            
                
    # Close settings
    def close(self):
        self.destroy()

