import os 
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from view.fonts import *
from CTkMessagebox import CTkMessagebox


class DeleteFiles(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.master = master
        self.title_label = ctk.CTkLabel(self, text=title, font=title_font())
        self.title_label.grid(row=0, column=0, pady=20)
        self.folder_path = None
        
        # Subtitle
        select_cols_label = ctk.CTkLabel(self, text="Select parent folder", font= heading_font())
        select_cols_label.grid(row=1, column = 0, sticky='ns', padx=50, pady=10, columnspan = 2)
        
        # Folder selection 
        self.folder_label = ctk.CTkLabel(self, text="Selected Folder: None", wraplength=300, font=("Helvetica", 12))
        self.folder_label.grid(row=2, column=0, columnspan=2, pady=5)
        
        select_cols_btn = ctk.CTkButton(self, text="Choose Folder", command=self.choose_folder)
        select_cols_btn.grid(row=3, column=0, padx=30, pady=10, columnspan = 2)

        # Dropdown
        combobox_var = ctk.StringVar()
        self.file_type_dropdown = ctk.CTkComboBox(self, values=['txt', 'pdf', 'exe', 'jpg', 'png', 'svg', 'xslx', 'csv', ], state='readonly', variable=combobox_var, command=self.dropdown_clicked)
        self.file_type_dropdown.grid(row=4, column=0, padx=50, pady=10, columnspan = 2)

        # Create textbox
        self.files_textbox = ctk.CTkTextbox(self, width = 300, height = 150, state='disabled')
        self.files_textbox.grid(row = 5, column = 0, pady=(25,25))

        # Delete Button
        self.delete_button = ctk.CTkButton(self, text='Delete', width=200, height=50, font=button_font(), command=self.delete_files)
        self.delete_button.grid(row=6,column=0,padx=(50, 50), pady=(15,50),sticky='s')

    # Choose a folder 
    def choose_folder(self):
        folder = filedialog.askdirectory()
        self.folder_path = folder
        self.folder_label.configure(text=f'Selected folder: {folder}')
            
    # Handling dropdown click        
    def dropdown_clicked(self, file_type):  
        
        self.files_textbox.configure(state='normal')
        self.files_textbox.delete('1.0', tk.END)
        
        # Handling file displayment
        matching_files = [file for file in os.listdir(self.folder_path) if file.endswith(f".{file_type}")]
        if matching_files:
            i = 0
            for file in matching_files:
                self.files_textbox.insert(tk.END,  f'({i+1}) {file}' + '\n')
                i+=1
        else:
            self.files_textbox.insert(tk.END, f"No .{file_type} files found in the selected folder.")
        self.files_textbox.configure(state='disabled')  
            
            
    # File deletion 
    def delete_files(self):
        file_type = self.file_type_dropdown.get().strip()
        # Logic for removing file
        if os.path.isdir(self.folder_path) and file_type:
            deleted_count = 0
            for file in os.listdir(self.folder_path):
                if file.endswith(f'.{file_type}'):
                    os.remove(os.path.join(self.folder_path, file))
                    deleted_count += 1
            CTkMessagebox(title='Success', message=f'All .{file_type} files deleted from {self.folder_path}.', icon="check", option_1='OK')
            self.files_textbox.configure(state='normal')
            self.files_textbox.delete('1.0', tk.END)
            self.files_textbox.insert(tk.END, f"No .{file_type} files found in the selected folder.")
            self.files_textbox.configure(state='disabled')
        else:
            CTkMessagebox(title="Error", message='Please select a valid folder and file type.', icon="cancel")
            
            