from flask import Flask, request, jsonify
from assistant import smart_response_text

app = Flask(__name__)

@app.route("/api/voice", methods=["POST"])
def voice():
    text = request.json.get("text")
    response = []
    def capture_output(txt):
        response.append(txt)
    smart_response_text(text, capture_output)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
