import customtkinter as ctk
from PIL import Image
from view.fonts import *
import pathlib
from view.delete_files import DeleteFiles
from view.organize_files import OrganizeFiles
from view.about import About
from view.settings import SettingsWindow

class Menu(ctk.CTkFrame):
    def __init__(self, master, title, default_gray, app_instance):
        super().__init__(master, corner_radius=0, width=300)
        self.app_instance = app_instance
        self.grid_columnconfigure(0, weight=1)  # Column for all widgets

        self.grid_rowconfigure(0, weight=0)  # Title row (fixed)
        self.grid_rowconfigure(1, weight=0)  # Organize button row (fixed)
        self.grid_rowconfigure(2, weight=0)  # Delete button row (fixed)
        self.grid_rowconfigure(3, weight=1)  # Settings button row (takes remaining space)
        
        self.toplevel_window = None
        
        self.title = title
        self.title = ctk.CTkLabel(self, text=self.title, corner_radius=6, font=title_font())
        self.title.grid(row=0, column=0, pady=(40,15), sticky='ew')
        
        self.organize_button = ctk.CTkButton(self, text='Organize', width=200, height=50, font=button_font(), command=self.show_organize_ui)
        self.organize_button.grid(row=1,column=0,padx=(50, 50), pady=(15,25),sticky='w')
        self.delete_button = ctk.CTkButton(self, text='Delete', width=200, height=50, font=button_font(), command=self.show_delete_ui)
        self.delete_button.grid(row=2,column=0,padx=(50, 50), pady=(25,0),sticky='w')
        
        img_path = pathlib.Path(__file__).parent.resolve().joinpath('src', 'img')
        
        # About button 
        about_img = Image.open(
            img_path.joinpath('about.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_about = ctk.CTkImage(about_img, size=(14,14))
        self.about_btn = ctk.CTkButton(self,text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='About', font=small_button_font(), image=self.img_about, width=85, command=self.show_about_ui)
        self.about_btn.grid(row=3, column=0, padx=(50,15), pady=(0,25), sticky='sw')
        
        # Settings button
        settings_image = Image.open(
            img_path.joinpath('settings.png')).resize((14,14), Image.Resampling.LANCZOS
        )
        self.img_settings = ctk.CTkImage(settings_image, size=(14, 14))
        self.settings_btn = ctk.CTkButton(self,text_color='#d6d6d6', fg_color='#2b2b2b', hover_color=default_gray, text='Settings', font=small_button_font(), image=self.img_settings, width=85, command=self.open_settings)
        self.settings_btn.grid(row=3, column=0, padx=(15,50), pady=(0,25), sticky='se')
    
    # Open Settings Window
    def open_settings(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SettingsWindow(self, self.master.DEFAULT_GRAY)
        else:
            self.toplevel_window.focus()
            
    def refresh_button_colors(self):
        """Refresh the colors of buttons to match the current theme."""
        current_fg_color = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        self.organize_button.configure(fg_color=current_fg_color)
        self.delete_button.configure(fg_color=current_fg_color)
    
    # UI's for right window
    def show_delete_ui(self):
        """Callback for the 'Delete' button to display Delete Files UI."""
        self.app_instance.show_delete_files_frame()
        
    def show_organize_ui(self):
        """Callback for the 'Organize' button to display Organize Files UI."""
        self.app_instance.show_organize_files_frame()
        
    def show_about_ui(self):
        """Callback for the 'About' button to display Main Page UI."""
        self.app_instance.show_about_frame()


class App(ctk.CTk):
    width = 900
    height = 600
    DEFAULT_GRAY = ('gray50', 'gray30')
    
    # ctk.set_appearance_mode("dark") 
    # ctk.set_default_color_theme("blue") 
    
    def __init__(self):
        super().__init__()
        
        self.title('FileTidy')
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)  
        self.iconbitmap(pathlib.Path(__file__).parent.resolve().joinpath('src', 'img', 'app_icon.ico'))
        self.grid_columnconfigure(0, minsize=300, weight = 0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Initialize starting frames
        self.menu_frame = Menu(self, 'Menu', self.DEFAULT_GRAY, self)
        self.menu_frame.grid(row=0,column=0, sticky='nsw')
        
        #self.about_frame.grid(row=0,column=1, padx=25, pady=25, sticky='nsew')
        self.about_frame = None
        
        self.delete_files_frame = None
        
        self.organize_files_frame = None
        
        # Current frame tracker
        self.current_frame = None
        
        # Show default frame (About)
        self.show_about_frame()
        
    # Display specified frame
    def show_delete_files_frame(self):
        if self.delete_files_frame is None:
            # Initialize DeleteFilesUI only when needed
            self.delete_files_frame = DeleteFiles(self, "Delete Files")
        self.switch_frame(self.delete_files_frame)
        
    def show_organize_files_frame(self):
        if self.organize_files_frame is None:
            self.organize_files_frame = OrganizeFiles(self, 'Organize Files')
        self.switch_frame(self.organize_files_frame)
        
    def show_about_frame(self):
        if self.about_frame is None:
            self.about_frame = About(self, 'About the Program')
        self.switch_frame(self.about_frame)
        
    def switch_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.grid_forget()  # Hide the current frame
        self.current_frame = frame
        self.current_frame.grid(row=0, column=1, padx=25, pady=25, sticky='nsew')    
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()