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

def get_response_from_text(inp):
    """
    Returns assistant response as a list of strings instead of speaking.
    This is for Flask + React integration.
    """
    responses = []

    def capture(txt):
        responses.append(txt)

    smart_response(inp, capture)
    return responses

def listen_and_respond(append_text):
    speak("Hello! I am listening. Say stop to exit.")
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
            break
