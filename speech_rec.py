import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
speech = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

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

            # Respond back
            speak(f"You said: {inp}")

            # Exit condition
            if inp.lower() in ["stop", "exit", "quit"]:
                speak("Goodbye! Have a great day.")
                break

    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Please try again.")
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
    except KeyboardInterrupt:
        speak("Program interrupted. Goodbye!")
        break
