from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "API is running"}), 200

@app.route("/health")
def health():
    return jsonify({"message": "healthy"}), 200

@app.route("/me")
def me():
    return jsonify({
        "name": "Mordecai Amehson",
        "email": "amehsonmordecai07@gmail.com",
        "github": "https://github.com/Hacker-Dark"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)