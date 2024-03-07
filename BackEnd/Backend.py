from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

uri = "mongodb+srv://Apiwit:192922@cluster0.k7xei6x.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["ShirtStore"]
collection = db["shirt",""]

@app.route("/")
def greet():
    return "<p>Welcome to SHIRTSTORE MART LAEMBANG.COM  </p>"

@app.route("/shirt", methods=["GET"])
def get_all_shirt():
    shirt = list(collection.find())
    return jsonify(shirt)

@app.route("/shirt/<int:shirt_id>", methods=["GET"])
def get_shirt(shirt_id):
    shirt = collection.find_one({"_id": shirt_id})
    if shirt:
        return jsonify(shirt)
    else:
        return jsonify({"error": "product not found"}), 404


@app.route("/shirt", methods=["POST"])
def create_shirt():
    data = request.get_json()
    existing_shirt = collection.find_one({"shirt_code": data["shirt_code"]})
    if existing_shirt:
        return jsonify({"error": "Shirt with the same product code already exists"}), 409
    else:
        collection.insert_one(data)
        return jsonify({"message": "Shirt created successfully"}), 201

@app.route("/shirt/<int:shirt_id>", methods=["PUT"])
def update_shirt(shirt_id):
    data = request.get_json()
    existing_shirt = collection.find_one({"_id": shirt_id})
    if existing_shirt:
        collection.update_one({"_id": shirt_id}, {"$set": data})
        updated_shirt = collection.find_one({"_id": shirt_id})
        return jsonify(updated_shirt)
    else:
        return jsonify({"error": "shirt not found"}), 404
    
@app.route("/shirt/<int:shirt_id>", methods=["DELETE"])
def delete_shirt(shirt_id):
    result = collection.delete_one({"_id": shirt_id})
    if result.deleted_count:
        return jsonify({"message": "Shirt deleted successfully"}), 200
    else:
        return jsonify({"error": "Shirt not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
