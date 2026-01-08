from flask import Flask, request, jsonify
import uuid
import hashlib
import datetime
import json

app = Flask(__name__)

# In-memory log store (replace with DB or S3 in production)
LOG_STORE = []

@app.route("/api/logs", methods=["POST"])
def create_log():
    body = request.get_json(force=True)

    payload = body.get("payload")
    actor = body.get("actor", "unknown")
    channel = body.get("channel", "user")

    if payload is None:
        return jsonify({"error": "payload is required"}), 400

    event_id = f"e:{uuid.uuid4().hex}"
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    meta = {"channel": channel}
    hash_input = payload + json.dumps(meta, sort_keys=True)
    event_hash = hashlib.sha256(hash_input.encode()).hexdigest()

    frame = {
        "e": event_id,
        "a": actor,
        "act": "utter",
        "payload": payload,
        "t": timestamp,
        "chan": channel,
        "hash": event_hash,
        "meta": meta
    }

    LOG_STORE.append(frame)
    return jsonify(frame), 201

@app.route("/api/logs/<event_id>", methods=["GET"])
def get_log(event_id):
    for frame in LOG_STORE:
        if frame["e"] == event_id:
            return jsonify(frame)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(port=8000, debug=True)
