import customtkinter
import customtkinter as ctk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import *
import os
#SET THEME/COLOR
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('AutoScribe')
root.iconbitmap('')
root.geometry('815x500')

#For text Select Video
root.file_label = ctk.CTkLabel(root, text="Select Video File:", text_color="white")
root.file_label.pack(pady=5)
root.file_label.place(x=175, y=30)

# text field for browse
root.file_entry = ctk.CTkEntry(root, width=400, placeholder_text="No file selected", state="normal")
root.file_entry.pack(pady=4)
root.file_entry.place(x=15, y=60)

my_button = customtkinter.CTkButton(root, text='Browse File')
my_button.pack(pady=80)
my_button.place(x=422, y=60)
#for youtube
root.file_entry = ctk.CTkEntry(root, width=400, placeholder_text="For Youtube Links Only", state="normal")
root.file_entry.pack(pady=4)
root.file_entry.place(x=15, y=100)

my_button = customtkinter.CTkButton(root, text='Open Youtube')
my_button.pack(pady=80)
my_button.place(x=422, y=100)

#For Select Language
root.file_label = ctk.CTkLabel(root, text="Select Language", text_color="white")
root.file_label.pack(pady=5)
root.file_label.place(x=175, y=130)


root.mainloop()