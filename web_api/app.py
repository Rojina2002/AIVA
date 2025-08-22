from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from assistant import smart_response

app = Flask(__name__)
CORS(app)

@app.route("/api/voice", methods=["POST"])
def voice():
    text = request.json.get("text")
    response = []
    def capture_output(txt):
        response.append(txt)
    smart_response(text, capture_output, tts=False)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
