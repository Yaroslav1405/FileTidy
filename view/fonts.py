import customtkinter as ctk

def get_font(family='Trebuchet MS', size=14, weight='normal', slant='roman', underline=False):
    
    return ctk.CTkFont(family=family, size=size, weight=weight, slant=slant, underline=underline)


def title_font():
    # Preset for title font
    return get_font(size=26, weight='bold')

def button_font(size=24):
    # Preset for buttons font
    return get_font(size=size, weight='bold')

def heading_font(size=22):
    # Preset for heading font
    return get_font(size=size, weight='normal')

def body_font(size=18):
    # Preset for body font (e.g. body text)
    return get_font(size=size)


def small_button_font(size=16):
    # Preset for small buttons font
    return get_font(size=size)

def link_font(size=12):
    # Preset for link font
    return get_font(size=size, underline=True)

def footer_font(size=12):
    # Preset for footer font
    return get_font(size=size)