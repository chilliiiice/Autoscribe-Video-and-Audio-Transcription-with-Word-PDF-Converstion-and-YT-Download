import customtkinter as ctk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
import os


# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AutoScribeApp(TkinterDnD.Tk):  # Inherit from TkinterDnD.Tk
    def __init__(self):
        super().__init__()
        self.title("AutoScribe - Video Transcriber")
        self.geometry("815x500")  # Set the window size to 815x500
        self.configure(bg="black")  # Set the background color to black

        # File selection
        self.file_label = ctk.CTkLabel(self, text="Select Video File:", fg_color="black", text_color="white")
        self.file_label.pack(pady=5)

        # Text field to display file location (using basic Entry widget for drag-and-drop)
        self.file_entry = ctk.CTkEntry(self, width=400, placeholder_text="No file selected", state="normal")
        self.file_entry.pack(pady=5)

        self.file_button = ctk.CTkButton(self, text="Browse", command=self.browse_file)
        self.file_button.pack(pady=5)

        # YouTube link input
        self.yt_label = ctk.CTkLabel(self, text="Or Enter YouTube Link:", fg_color="black", text_color="white")
        self.yt_label.pack(pady=5)
        self.yt_entry = ctk.CTkEntry(self, width=400)
        self.yt_entry.pack(pady=5)

        # Drag and Drop Box
        self.drop_label = ctk.CTkLabel(self, text="Drag & Drop Video Here", height=100, width=400, fg_color="gray",
                                       text_color="white")
        self.drop_label.pack(pady=10)

        # Register drag-and-drop target
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.on_drop)

        # Language selection
        self.lang_label = ctk.CTkLabel(self, text="Select Language:", fg_color="black", text_color="white")
        self.lang_label.pack(pady=5)
        self.lang_option = ctk.CTkComboBox(self, values=["Auto-Detect", "English", "Spanish", "French", "German"])
        self.lang_option.pack(pady=5)

        # Progress Bar
        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.pack(pady=10)
        self.progress.set(0)

        # Export Options
        self.export_label = ctk.CTkLabel(self, text="Export As:", fg_color="black", text_color="white")
        self.export_label.pack(pady=5)
        self.export_option = ctk.CTkComboBox(self, values=["TXT", "PDF", "Word"])
        self.export_option.pack(pady=5)

        # Start Button
        self.start_button = ctk.CTkButton(self, text="Start Transcription", command=self.start_transcription)
        self.start_button.pack(pady=20)



    def update_file_path(self, file_path):
        self.file_entry.configure(state="normal")  # Enable the text field to edit
        self.file_entry.delete(0, "end")  # Clear any previous value
        self.file_entry.insert(0, file_path)  # Insert the file path into the text field
        self.file_entry.configure(state="readonly")  # Set back to readonly

    def start_transcription(self):
        file_path = self.file_entry.get()
        if file_path:
            print(f"Starting transcription for: {file_path}")  # Replace with actual transcription logic
        self.progress.set(0.5)  # Simulating progress update

    def on_drop(self, event):
        # Get the dropped file path from event data
        file_path = event.data
        # Ensure it's a valid file path
        if file_path and os.path.isfile(file_path):
            self.update_file_path(file_path)
            print(f"Dropped file: {file_path}")  # Replace with actual file handling logic


if __name__ == "__main__":
    app = AutoScribeApp()
    app.mainloop()
