from flask import Flask

PORT = 8000
MESSAGE = "Hello, World"

app = Flask(__name__)

@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result

if __name__ == "__main__":
    app.run(debug= True, port=PORT)
    
    







