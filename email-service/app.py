from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def email_home():
    return jsonify({"email": "Email service running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7600)
