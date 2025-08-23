import datetime
import webbrowser

# Smart responses (text-only)
def smart_response(inp, append_text, tts=False):
    inp_lower = inp.lower()

    if "hello" in inp_lower or "hi" in inp_lower:
        append_text("Assistant: Hello! How are you today?")
        return "Hello! How are you today?" if tts else None

    elif "how are you" in inp_lower:
        append_text("Assistant: I am just a program, but I'm doing great! How about you?")
        return "I am just a program, but I'm doing great! How about you." if tts else None

    elif "time" in inp_lower:
        now = datetime.datetime.now().strftime("%H:%M")
        append_text(f"Assistant: The current time is {now}")
        return f"The current time is {now}" if tts else None

    elif "date" in inp_lower:
        today = datetime.datetime.now().strftime("%d %B %Y")
        append_text(f"Assistant: Today's date is {today}")
        return f"Today's date is {today}" if tts else None

    elif "play" in inp_lower or "song" in inp_lower or "gana" in inp_lower:
        query = inp.replace("play", "").replace("song", "").replace("gana", "").strip()
        append_text(f"Assistant: Playing {query} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Playing {query} on YouTube" if tts else None

    elif inp_lower in ["stop", "exit", "quit"]:
        append_text("Assistant: Goodbye! Have a great day.")
        return "Goodbye! Have a great day."

    else:
        append_text(f"You said: {inp}")
        return f"You said: {inp}" if tts else None

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
