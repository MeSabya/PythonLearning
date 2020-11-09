from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/status", methods=['PUT'])
def status():
    print("request.method", request.method)
    body = request.get_json(force=True)
    if request.method == 'PUT':
        print(f"Received status {body['status']}")
        return '', 200


@app.route("/heartbeat", methods=["PUT"])
def heartbeat():
    print("Received heartbeat")
    return "", 200


if __name__ == "__main__":
    app.run()
