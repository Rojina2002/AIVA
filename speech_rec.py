import speech_recognition as sr

# Initialize recognizer
speech = sr.Recognizer()

print("Python Voice Assistant is Listening! Say 'stop' to exit.")

while True:
    try:
        with sr.Microphone() as source:
            # Reduce noise impact
            speech.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            
            # Capture audio
            audio = speech.listen(source)

            # Recognize speech using Google API
            inp = speech.recognize_google(audio)
            print(f"You said: {inp}")

            # Exit condition
            if inp.lower() in ["stop", "exit", "quit"]:
                print("Exiting program. Goodbye!")
                break

    except sr.UnknownValueError:
        print("Sorry, I could not understand that. Please try again.")
    except sr.RequestError:
        print("Network error or API unavailable.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
        break
