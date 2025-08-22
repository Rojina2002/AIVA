# AIVA - AI Voice Assistant

AIVA is a smart voice assistant designed to help you with daily tasks via voice commands. You can interact with it through a Python desktop GUI or a web interface.

## Features

* Responds to greetings and simple queries
* Provides current time and date
* Plays songs on YouTube
* Continuous listening until stopped
* Web version with live voice input using React and Flask API

## Technologies Used

* **Backend:** Python, Flask, pyttsx3, SpeechRecognition
* **Frontend:** React, Axios
* **GUI:** Tkinter
* **Other:** Web browser integration for YouTube, CORS handling

## Getting Started

### Desktop App

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/AIVA.git
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the desktop assistant:

   ```bash
   python main.py
   ```

### Web App

1. Navigate to the web\_app folder:

   ```bash
   cd web_app
   ```
2. Install dependencies:

   ```bash
   npm install
   ```
3. Start the React app:

   ```bash
   npm start
   ```
4. Start the Flask API (in the web\_api folder):

   ```bash
   python app.py
   ```

## Usage

* Press the "Talk to Assistant" button in the web app or start the desktop GUI.
* Speak your commands (Hello, time, date, play \[song], stop, etc.).
* The assistant will respond and perform actions accordingly.

## Suggested Commands

* Hi / Hello
* What time is it?
* What’s today’s date?
* Play \[song name]
* Stop / Exit

## License

This project is open-source and free to use.
