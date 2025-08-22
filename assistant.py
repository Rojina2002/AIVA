import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

speech = sr.Recognizer()
engine = pyttsx3.init()

# Text-to-speech
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Smart responses
def smart_response(inp, append_text):
    inp_lower = inp.lower()

    if "hello" in inp_lower or "hi" in inp_lower:
        speak("Hello! How are you today?")
        append_text("Assistant: Hello! How are you today?")
    elif "how are you" in inp_lower:
        speak("I am just a program, but I'm doing great! How about you?")
        append_text("Assistant: I am just a program, but I'm doing great! How about you?")
    elif "time" in inp_lower:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
        append_text(f"Assistant: The current time is {now}")
    elif "date" in inp_lower:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
        append_text(f"Assistant: Today's date is {today}")
    elif "play" in inp_lower or "song" in inp_lower or "gana" in inp_lower:
        speak(f"Playing {inp} on YouTube")
        append_text(f"Assistant: Playing {inp} on YouTube")
        query = inp.replace("play", "").replace("song", "").replace("gana", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif inp_lower in ["stop", "exit", "quit"]:
        speak("Goodbye! Have a great day.")
        append_text("Assistant: Goodbye! Have a great day.")
        return False
    else:
        speak(f"You said: {inp}")
        append_text(f"You said: {inp}")
    return True
