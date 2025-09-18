from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def orders_home():
    return jsonify({"orders": "Orders service running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7100)
