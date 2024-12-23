import time
import os 
import shutil
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from view.fonts import *
import pathlib
 

class Menu(ctk.CTkFrame):
    def __init__(self, master, title, default_gray):
        super().__init__(master, corner_radius=0, width=300)
        
        self.grid_columnconfigure(0, weight=1)  # Column for all widgets

        self.grid_rowconfigure(0, weight=0)  # Title row (fixed)
        self.grid_rowconfigure(1, weight=0)  # Organize button row (fixed)
        self.grid_rowconfigure(2, weight=0)  # Delete button row (fixed)
        self.grid_rowconfigure(3, weight=1)  # Settings button row (takes remaining space)
        
        self.toplevel_window = None
        
        self.title = title
        self.title = ctk.CTkLabel(self, text=self.title, corner_radius=6, font=title_font())
        self.title.grid(row=0, column=0, pady=(40,15), sticky='ew')
        
        self.organize_button = ctk.CTkButton(self, text='Organize', width=200, height=50, font=button_font())
        self.organize_button.grid(row=1,column=0,padx=(50, 50), pady=(15,25),sticky='w')
        self.delete_button = ctk.CTkButton(self, text='Delete', width=200, height=50, font=button_font())
        self.delete_button.grid(row=2,column=0,padx=(50, 50), pady=(25,0),sticky='w')
        
        img_path = pathlib.Path(__file__).parent.resolve().joinpath('src', 'img')
        
        # About button 
        about_img = Image.open(
            img_path.joinpath('about.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_about = ctk.CTkImage(about_img, size=(14,14))
        self.about_btn = ctk.CTkButton(self,text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='About', font=small_font(), image=self.img_about, width=85)
        self.about_btn.grid(row=3, column=0, padx=(50,15), pady=(0,25), sticky='sw')
        
        # Settings button
        settings_image = Image.open(
            img_path.joinpath('settings.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_settings = ctk.CTkImage(settings_image, size=(14, 14))
        self.settings_btn = ctk.CTkButton(self,text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='Settings', font=small_font(), image=self.img_settings, width=85, command=self.open_settings)
        self.settings_btn.grid(row=3, column=0, padx=(15,50), pady=(0,25), sticky='se')
    
    # Open Settings Window
    def open_settings(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SettingsWindow(self, self.master.DEFAULT_GRAY)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
            
    def refresh_button_colors(self):
        """Refresh the colors of buttons to match the current theme."""
        current_fg_color = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        self.organize_button.configure(fg_color=current_fg_color)
        self.delete_button.configure(fg_color=current_fg_color)


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, master, default_gray):
        self.mode = 'dark'
        self.current_theme = 'blue'
        super().__init__(master)
        self.geometry("400x300")
        self.configure(bg='#2b2b2b')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title row
        self.grid_rowconfigure(1, weight=0)  # Mode Switch button (fixed)
        self.grid_rowconfigure(2, weight = 0) # Theme Switch button (fixed)
        
        
        self.label = ctk.CTkLabel(self, text="Settings", font=title_font())
        self.label.grid(row = 0, column = 0, pady=(15,10))
        img_path = pathlib.Path(__file__).parent.resolve().joinpath('src', 'img')
        
        # Mode setting
        mode_img = Image.open(
            img_path.joinpath('mode_switch.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_mode = ctk.CTkImage(mode_img, size=(14,14))
        self.change_mode_btn = ctk.CTkButton(self, text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='Switch Mode', font=small_font(), image=self.img_mode, command=self.change_mode)
        self.change_mode_btn.grid(row=1, column=0, pady = (10,5), sticky='ns')
        
        # Theme setting
        theme_img = Image.open(
            img_path.joinpath('theme_switch.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_theme = ctk.CTkImage(theme_img, size=(14,14))
        color = ["blue", "green", "dark-blue"]
        self.theme_option = ctk.CTkOptionMenu(self, values = color, command = self.change_theme)
        self.theme_option.grid(row=2, column=0, pady=(5,0), sticky='ns')
        #self.change_theme_btn = ctk.CTkButton(self, text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='Switch Theme', font=small_font(), image=self.img_theme, command=self.change_theme)
        #self.change_theme_btn.grid(row=2, column=0, pady= (5,0), sticky='ns')
        
    
    
        
    def change_mode(self):
        if self.mode == 'dark':
            ctk.set_appearance_mode("light")
            self.mode = 'light'
        else:
            ctk.set_appearance_mode('dark')
            self.mode = 'dark' 
            
    def change_theme(self,choice):
        # Switch to the new theme
        ctk.set_default_color_theme(choice)

                
    # Close settings
    def close(self):
        self.destroy()


class About(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master, corner_radius=10) 
        
        
        
        self.title = title
        self.title = ctk.CTkLabel(self, text=self.title, font=title_font())
        self.title.grid(row=0, column=1, pady=(40,25))
        self.about_text = "This program is made to help organize or delete user’s files in few clicks."
        self.description = ctk.CTkLabel(self, text=self.about_text, wraplength=400, justify='center', font=body_font())
        self.description.grid(row=1,column=1, padx=(75,75), pady=(25,0), sticky='n')


class App(ctk.CTk):
    width = 900
    height = 600
    DEFAULT_GRAY = ('gray50', 'gray30')
    # ctk.set_appearance_mode("dark") 
    # ctk.set_default_color_theme("blue") 
    
    def __init__(self):
        super().__init__()
        
        self.title('File Organizer')
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)  
        self.grid_columnconfigure(0, minsize=300, weight = 0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.menu_frame = Menu(self, 'Menu', self.DEFAULT_GRAY)
        self.menu_frame.grid(row=0,column=0, sticky='nsw')
        self.about_frame = About(self, 'About the Program')
        self.about_frame.grid(row=0,column=1, padx=25, pady=25, sticky='nsew')
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()