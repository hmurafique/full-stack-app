from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def notify_home():
    return jsonify({"notifications": "Notifications service running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7200)
