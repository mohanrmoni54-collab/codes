from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet')
def greet():
    return jsonify(message="Hello, User!")

if __name__ == "__main__":
    app.run()
