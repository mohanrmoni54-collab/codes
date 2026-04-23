from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet')
def greet():
    return jsonify(message="Hello, User!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



Dockerfile
# Use official Python image
FROM python:3.9-slim
# Set working directory
WORKDIR /app
# Copy files
COPY . /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port
EXPOSE 5000
# Run application
CMD ["python", "app.py"]

requirements.txt
flask





docker build -t flask-app .
docker run -p 5000:5000 flask-app

open in browser
http://localhost:5000/greet
