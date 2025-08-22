import threading
import tkinter as tk
from tkinter import scrolledtext
from assistant import listen_and_respond

# GUI helper
def append_text(text):
    text_area.config(state='normal')
    text_area.insert(tk.END, text + "\n")
    text_area.see(tk.END)
    text_area.config(state='disabled')

# Show suggested commands on start
def show_suggestions():
    suggestions = [
        "Hello",
        "How are you?",
        "What is the time?",
        "What is the date?",
        "Play <song_name>",
        "Stop"
    ]
    append_text("💡 Suggested things to ask:")
    for s in suggestions:
        append_text(f"- {s}")
    append_text("")  # blank line for spacing

# Listening loop in a separate thread
def run_listen():
    listen_and_respond(append_text)

# GUI setup
root = tk.Tk()
root.title("Smart Voice Assistant")
root.geometry("500x450")

# Text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Display suggestions on start
show_suggestions()

# Start listening thread
threading.Thread(target=run_listen, daemon=True).start()

root.mainloop()
