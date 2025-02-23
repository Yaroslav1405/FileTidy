import os 
import shutil
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from view.fonts import *
from CTkMessagebox import CTkMessagebox


class OrganizeFiles(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.master = master
        self.folder_path = None
        
        # Title
        self.title_label = ctk.CTkLabel(self, text=title, font=title_font())
        self.title_label.grid(row=0, column=0, pady=20)
        
        # Subtitle
        select_cols_label = ctk.CTkLabel(self, text="Select parent folder", font= heading_font())
        select_cols_label.grid(row=1, column = 0, sticky='ns', padx=50, pady=10, columnspan = 2)
        
        # Folder selection 
        self.folder_label = ctk.CTkLabel(self, text="Selected Folder: None", wraplength=300, font=("Helvetica", 12))
        self.folder_label.grid(row=2, column=0, columnspan=2, pady=5)
        
        select_cols_btn = ctk.CTkButton(self, text="Choose Folder", command=self.choose_folder)
        select_cols_btn.grid(row=3, column=0, padx=30, pady=10, columnspan = 2)

        # Create textbox
        self.files_textbox = ctk.CTkTextbox(self, width = 300, height = 150, state='disabled')
        self.files_textbox.grid(row = 5, column = 0, pady=(25,25))

        # Delete Button
        self.delete_button = ctk.CTkButton(self, text='Organize', width=200, height=50, font=button_font(), command=self.organize_files)
        self.delete_button.grid(row=6,column=0,padx=(50, 50), pady=(15,50),sticky='s')


    # Folder selection
    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            
            self.folder_path = folder           
            self.folder_label.configure(text=f'Selected folder: {folder}')
            self.files_textbox.configure(state='normal')
            self.files_textbox.delete('1.0', tk.END)
            
            # Collect Files
            #   Check length of the folder
            if not len(os.listdir(folder)) == 0:
                i = 0
                # Handling file displayment
                for file in os.listdir(folder):
                    file_path = os.path.join(folder, file)
                    if os.path.isfile(file_path):
                        self.files_textbox.insert(tk.END,  f'({i+1}) {file}' + '\n')
                        i+=1
                # Handling empty folder       
                if i == 0:
                    self.files_textbox.insert(tk.END, f"No files found in the selected folder.")
            # Handling very empty folder :)
            else:
                self.files_textbox.insert(tk.END, f"This folder is completely empty.")

            self.files_textbox.configure(state='disabled')       
        

    # File organization 
    def organize_files(self):
        
        
        sub_folder = {
                    'Excel Files': [".xlsx", ".xls", ".csv", ".xlsm", ".xlsb", ".ods"],
                    'Text Files': [".txt", ".log", ".md", ".rtf", ".doc", ".docx"],
                    'PDF Files': [".pdf"],
                    'Images': [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
                    'Executable Files': [".exe", ".bat", ".sh", ".app", ".jar"],
                    'Other Files': []
                    }
        
        all_files = os.listdir(self.folder_path)
        if not all_files:
            CTkMessagebox(title="Error", message='Please select a valid folder.', icon="cancel")
            
        else:
            # Loop through dictionary
            for sub in sub_folder:
                full_path = os.path.join(self.folder_path, sub)
                # Create subfolders if they don't exist
                if not os.path.exists(full_path):
                    os.makedirs(full_path, exist_ok=True) 
                
                extensions = set(sub_folder[sub])
                # Move matching files
                for file in all_files:
                    if any(file.endswith(ext) for ext in extensions):  
                        shutil.move(os.path.join(self.folder_path, file), full_path)
            # Handle files with other extensions                       
            for file in os.listdir(self.folder_path):
                dest_file = os.path.join(self.folder_path, file)
                if os.path.isfile(dest_file):
                    shutil.move(dest_file, os.path.join(self.folder_path, "Other Files"))
          
            """HANDLE ISSUE WITH SAME FILE NAMES"""          
                    
            CTkMessagebox(title='Success', message=f'All files were organized into folders.', icon="check", option_1='OK')            
            self.files_textbox.configure(state='normal')         
            self.files_textbox.delete('1.0', tk.END)
            self.files_textbox.insert(tk.END, f"No files found in the selected folder.")
            self.files_textbox.configure(state='disabled')
            
            
        