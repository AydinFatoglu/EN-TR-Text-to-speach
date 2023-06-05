import tkinter as tk
from tkinter import scrolledtext
from gtts import gTTS
import subprocess
import os
import threading

def center_window(root):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position of the window
    window_width = 500
    window_height = 400
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window's position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Multilingual Text-to-Speech")

        # Create input text box with scrollbars
        self.input_box = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10)
        self.input_box.pack()

        # Create right-click context menu
        self.context_menu = tk.Menu(master, tearoff=0)
        self.context_menu.add_command(label="Cut", command=self.cut_text)
        self.context_menu.add_command(label="Copy", command=self.copy_text)
        self.context_menu.add_command(label="Paste", command=self.paste_text)
        self.context_menu.add_command(label="Select All", command=self.select_all_text)

        # Bind right-click event to show the context menu
        self.input_box.bind("<Button-3>", self.show_context_menu)

        # Create language selection dropdown
        self.language_label = tk.Label(master, text="Select language:")
        self.language_label.pack()
        self.languages = {"English": "en", "Turkish": "tr"}
        self.selected_language = tk.StringVar()
        self.language_dropdown = tk.OptionMenu(master, self.selected_language, *self.languages.keys())
        self.language_dropdown.pack()

        # Create submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.generate_speech)
        self.submit_button.pack()

        # Create stop button
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_speech, state=tk.DISABLED)
        self.stop_button.pack()

        # Create loading label
        self.loading_label = tk.Label(master, text="")
        self.loading_label.pack()

        # Process object for sound playback
        self.playback_process = None

    def show_context_menu(self, event):
        # Show the context menu at the right-click position
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def cut_text(self):
        self.input_box.event_generate("<<Cut>>")

    def copy_text(self):
        self.input_box.event_generate("<<Copy>>")

    def paste_text(self):
        self.input_box.event_generate("<<Paste>>")

    def select_all_text(self):
        self.input_box.tag_add("sel", "1.0", "end")

    def generate_speech(self):
        # Get input text and selected language
        input_text = self.input_box.get("1.0", "end-1c")
        language = self.languages[self.selected_language.get()]

        # Disable the submit button and change its text
        self.submit_button.config(state=tk.DISABLED, text="Generating...")

        # Create a separate thread for speech generation and playback
        threading.Thread(target=self.process_speech, args=(input_text, language)).start()

    def process_speech(self, input_text, language):
        # Use gTTS to generate speech and save to file
        tts = gTTS(text=input_text, lang=language)
        tts.save("speech.mp3")

        # Update loading label
        self.loading_label.config(text="Playing sound...")

        # Enable the stop button
        self.stop_button.config(state=tk.NORMAL)

        # Play speech file
        self.playback_process = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "speech.mp3"])

        # Wait for sound playback to finish
        self.playback_process.wait()

        # Update loading label
        self.loading_label.config(text="Cleaning up...")

        # Delete speech file
        os.remove("speech.mp3")

        # Update loading label
        self.loading_label.config(text="")

        # Disable the stop button
        self.stop_button.config(state=tk.DISABLED)

        # Enable the submit button and restore its text
        self.submit_button.config(state=tk.NORMAL, text="Submit")

    def stop_speech(self):
        if self.playback_process:
            # Terminate the sound playback process
            self.playback_process.terminate()

root = tk.Tk()
root.title("Multilingual Text-to-Speech App")

# Center the window
center_window(root)

# Disable maximizing the window
root.resizable(False, False)

app = TextToSpeechApp(root)
root.mainloop()

