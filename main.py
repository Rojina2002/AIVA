import threading
import tkinter as tk
from tkinter import scrolledtext
##import speech_recognition as sr
from assistant import listen_and_respond

speech = sr.Recognizer()

# GUI helper
def append_text(text):
    text_area.config(state='normal')
    text_area.insert(tk.END, text + "\n")
    text_area.see(tk.END)
    text_area.config(state='disabled')

# Listening loop
def run_listen():
    listen_and_respond(append_text)

    '''speak("Hello! I am listening. Say stop to exit.")
    append_text("Assistant: Hello! I am listening. Say stop to exit.")
    running = True
    while running:
        try:
            with sr.Microphone() as source:
                speech.adjust_for_ambient_noise(source, duration=0.5)
                append_text("Listening...")
                audio = speech.listen(source)
                inp = speech.recognize_google(audio)
                append_text(f"You said: {inp}")
                running = smart_response(inp, append_text)
        except sr.UnknownValueError:
            speak("Sorry, I could not understand that. Please try again.")
            append_text("Assistant: Sorry, I could not understand that. Please try again.")
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            append_text("Assistant: Network error. Please check your internet connection.")
        except KeyboardInterrupt:
            speak("Program interrupted. Goodbye!")
            append_text("Assistant: Program interrupted. Goodbye!")
            break'''

# GUI setup
root = tk.Tk()
root.title("Smart Voice Assistant")
root.geometry("500x400")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Start listening thread
threading.Thread(target=run_listen, daemon=True).start()

root.mainloop()
