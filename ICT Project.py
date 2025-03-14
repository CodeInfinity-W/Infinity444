import pyttsx3
import customtkinter
from tkinter import filedialog

from cus import entry


def ebook_voice_reader(voice):
    voice_stimulator = pyttsx3.init(voice)
    all_available_voices = voice_stimulator.getProperty('voices')
    voice_stimulator.setProperty('voice',all_available_voices[1].id)
    voice_stimulator.setProperty('volume', 0.8 )
    voice_stimulator.setProperty('rate', 100)
    def read_text():
        text = entry.get("0.0", "end").strip()  # Get the text from the textbox
        if text:
            voice_stimulator.say(text)  # Send text to the TTS engine
            voice_stimulator.runAndWait()


def ebook_extractor(filename):
    with open(filename, 'r') as f:
        text_file = f.read()
        ebook_voice_reader(text_file)

def file_loader():
    file_path = filedialog.askopenfilename(title="Load file", filetypes=[("Text Files", "*.txt")])
    if file_path:

        entry.delete(0, customtkinter.END)
        entry.insert(0, file_path)

def play_audio():
    file_path = entry.get()  # Get the file path from the entry widget
    if file_path:
        ebook_extractor(file_path)  # If a file path is present, extract and read the file aloud
    else:
        print("No file selected")


def main():
    global entry  # Make the entry widget globally accessible
    window = customtkinter.CTk()
    window.title("E-Book Reader")
    window.geometry("600x400")
    window._set_appearance_mode("dark")

    frame = customtkinter.CTkFrame(window, width=490, height=300, fg_color="white")
    frame.place(relx = 0.1, rely = 0.1)

    label = customtkinter.CTkLabel(frame, text="CONTENT OF TEXT FILE", text_color="black")
    label.place(relx = 0.08, rely = 0.1)

    nav_frame = customtkinter.CTkFrame(window, width=600, height=30, fg_color="gray")
    nav_frame.place(relx=0, rely=0)

    title = customtkinter.CTkLabel(nav_frame, text="EBOOK READER", font=("ADLaM Display", 20), text_color="black")
    title.place(relx=0.1, rely=0.2)

    # Create the entry widget
    entry = customtkinter.CTkEntry(window, placeholder_text="📂 File Directory", width=200, font=("algeria", 15))
    entry.place(relx=0.0, rely=0.9)

    btn_display = customtkinter.CTkButton(window, text="DISPLAY", width=80 , fg_color= 'blue')
    btn_display.place(relx = 0.35, rely = 0.9)

    # Load file button
    load = customtkinter.CTkButton(window, text="Load File", font=("algeria", 15), fg_color="blue")
    load.place(relx=0.50, rely=0.9)
    load.configure(command=file_loader)  # Directly use the file_loader function

    # Play button
    play = customtkinter.CTkButton(window, text="🔊Play", font=("algeria", 15), fg_color="blue")
    play.place(relx=0.75, rely=0.9)
    play.configure(command=play_audio)  # Directly use the play_audio function



    window.mainloop()


main()