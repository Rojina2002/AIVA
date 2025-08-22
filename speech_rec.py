import speech_recognition as sr
speech=sr.Recognizer()
print("Python is Listening!")
with sr.Microphone() as source:
  speech.adjust_for_ambient_noise(source)
  audio=speech.listen(source)
  inp=speech.recognize_google(audio)
print(f'You said: {inp}')