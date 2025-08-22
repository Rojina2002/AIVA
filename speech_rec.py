import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer and TTS engine
speech = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to handle smart responses
def smart_response(inp):
    inp_lower = inp.lower()

    if "hello" in inp_lower or "hi" in inp_lower:
        speak("Hello! How are you today?")
    elif "how are you" in inp_lower:
        speak("I am just a program, but I'm doing great! How about you?")
    elif "time" in inp_lower:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in inp_lower:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
    elif "play" in inp_lower or "song" in inp_lower or "gana" in inp_lower:
        speak(f"Playing {inp} on YouTube")
        query = inp.replace("play", "").replace("song", "").replace("gana", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif inp_lower in ["stop", "exit", "quit"]:
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak(f"You said: {inp}")
    return True

speak("Hello! I am listening. Say stop to exit.")

while True:
    try:
        with sr.Microphone() as source:
            # Adjust for background noise
            speech.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")

            # Capture audio
            audio = speech.listen(source)

            # Convert speech to text
            inp = speech.recognize_google(audio)
            print(f"You said: {inp}")

            # Smart response
            if not smart_response(inp):
                break

    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Please try again.")
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
    except KeyboardInterrupt:
        speak("Program interrupted. Goodbye!")
        break
