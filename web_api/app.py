from flask import Flask, request, jsonify, send_from_directory
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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
