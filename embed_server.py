from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import logging

# initialize Flask app and SentenceTransformer model
app = Flask(__name__)
# setup model
model = SentenceTransformer('all-MiniLM-L6-v2')

# define a route for embedding
@app.route("/embed", methods=["POST"])
def embed():
    # Check if the request contains JSON data
    data = request.get_json()
    if not data:
        # Log the error
        logging.warning("Invalid JSON data received")
        # response
        return jsonify({"error": "Invalid JSON"}), 400
    
    # check if the 'text' field is present in the JSON data
    text = data.get("text")
    if not text:
        # Log the error
        logging.warning("Missing 'text' field in JSON data")
        # response
        return jsonify({"error": "Missing 'text'"}), 400

    # generate the embedding for the provided text
    embedding = model.encode(text).tolist()

    # log request content and embedding summary
    logging.info(f"Text received: {text[:100]}... (length: {len(text)} chars)")
    logging.info(f"Generated embedding with {len(embedding)} dimensions")

    # Return the embedding as a JSON response
    return jsonify({"embedding": embedding})

# define a route for health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
