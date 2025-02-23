import customtkinter as ctk
from view.fonts import *
import webbrowser

class About(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master, corner_radius=10) 
        self.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Title row (fixed)
        self.grid_rowconfigure(1, weight=0) # Description row (fixed)
        self.grid_rowconfigure(2, weight=0) # Contact row (fixed)
        self.grid_rowconfigure(3, weight=1) # Footer row (remaining space)
        self.master = master
        
        # Title
        self.title = ctk.CTkLabel(self, text=title, font=title_font())
        self.title.grid(row=0, column=1, pady=(40,25))
        
        # Program description
        self.about_text = "FileTidy is a simple tool designed to help the user organize and clean up files with ease. \
            Select a folder, sort files into subfolders, or delete unwanted ones — all in a few clicks. Keep your workspace neat and clutter-free effortlessly."
        self.description = ctk.CTkLabel(self, text=self.about_text, wraplength=400, justify='center', font=body_font())
        self.description.grid(row=1,column=1, padx=75, pady=25, sticky='n')
        
        # Contact section
        self.contact_text = "For any questions: "
        self.link_text = "Contact me"

        # Plain text label
        contact_label = ctk.CTkLabel(self, text=self.contact_text, font=footer_font())
        contact_label.grid(row=3, column=1, pady=(0,25), sticky='sw')

        # Hyperlink label
        link = ctk.CTkLabel(self, text=self.link_text, cursor="hand2", font=link_font())
        link.bind("<Button-1>", lambda e: self.open_link("https://linktr.ee/yaroslavhinda"))
        link.grid(row=3, column=1, pady=(0,5), sticky='sw')

        
        # Footer section
        self.created_by_text = 'Created By Yaroslav Hinda'
        created_by = ctk.CTkLabel(self, text=self.created_by_text, font=footer_font())
        created_by.grid(row=3,column=1, padx=(0,15), columnspan=2, pady=(0,5), sticky='se')       
        
        
    def open_link(self, url):
        webbrowser.open_new(url)
