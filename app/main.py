from flask import Flask
import requests
import json

app = Flask(__name__)

urls = [
    "http://time-service.default.svc.cluster.local:6001", # this one!
    # {"successes": [
    #     "Hello from Python (http://time-service.default.svc.cluster.local:6001)! b'The time is 2023-04-12 19:51:59.464179', The time is 2023-04-12 19:51:59.464179"],
    #  "failures": []}
]

@app.route("/")
def hello():
    successes = []
    failures = []
    for url in urls:
        try:
            x = requests.get(url)
            successes.append(f"Hello from Python ({url})! {x.content}, {x.text}")
        except Exception as e:
            failures.append(f"Goodbye ({url}). ERROR: {e}")
    return json.dumps({"successes": successes, "failures": failures})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
