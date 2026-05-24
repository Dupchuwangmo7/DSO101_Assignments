from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the CI/CD Demo API!",
        "status": "running",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify({"result": a * b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
