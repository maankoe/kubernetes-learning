from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def time():
    return f"The time is {datetime.now()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
