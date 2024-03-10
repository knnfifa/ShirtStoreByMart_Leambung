from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

uri = "mongodb+srv://Apiwit:192922@cluster0.k7xei6x.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["SHIRTSTOREBYMARTLAEMBANG"]
collections = {
    "collection1": db["shirtmanu"],
    "collection2": db["shirtmancity"],
    "collection3": db["shirtLiver"],
    "collection4": db["shirtarsenal"]
}

@app.route("/")
def greet():
    return "<p>Welcome to SHIRTSTORE MART LAEMBANG.COM  </p>"

@app.route("/shirtmanu", methods=["GET"])
def get_all_shirtmanu():
    shirtmanu = list(collections["collection1"].find())
    return jsonify(shirtmanu)

@app.route("/shirtmanu/<int:shirtmanu_id>", methods=["GET"])
def get_shirtmanu(shirtmanu_id):
    shirtmanu = collections["collection1"].find_one({"_id": shirtmanu_id})
    if shirtmanu:
        return jsonify(shirtmanu)
    else:
        return jsonify({"error": "product not found"}), 404


@app.route("/shirtmanu", methods=["POST"])
def create_shirtmanu():
    data = request.get_json()
    existing_shirtmanu = collections["collection1"].find_one({"shirtmanu_code": data["shirtmanu_code"]})
    if existing_shirtmanu:
        return jsonify({"error": "Shirt with the same product code already exists"}), 409
    else:
        collections["collection1"].insert_one(data)
        return jsonify({"message": "Shirt created successfully"}), 201

@app.route("/shirtmanu/<int:shirtmanu_id>", methods=["PUT"])
def update_shirtmanu(shirtmanu_id):
    data = request.get_json()
    existing_shirtmanu = collections["collection1"].find_one({"_id": shirtmanu_id})
    if existing_shirtmanu:
        collections["collection1"].update_one({"_id": shirtmanu_id}, {"$set": data})
        updated_shirtmanu = collections["collection1"].find_one({"_id": shirtmanu_id})
        return jsonify(updated_shirtmanu)
    else:
        return jsonify({"error": "shirt not found"}), 404
    
@app.route("/shirtmanu/<int:shirtmanu_id>", methods=["DELETE"])
def delete_shirtmanu(shirtmanu_id):
    result = collections["collection1"].delete_one({"_id": shirtmanu_id})
    if result.deleted_count:
        return jsonify({"message": "Shirt deleted successfully"}), 200
    else:
        return jsonify({"error": "Shirt not found"}), 404
    
# -------------------------------------------------------------------------------------------------------

@app.route("/shirtmancity", methods=["GET"])
def get_all_shirtmancity():
    shirtmancity = list(collections["collection2"].find())
    return jsonify(shirtmancity)

@app.route("/shirtmancity/<int:shirtmancity_id>", methods=["GET"])
def get_shirtmancity(shirtmancity_id):
    shirtmancity = collections["collection2"].find_one({"_id": shirtmancity_id})
    if shirtmancity:
        return jsonify(shirtmancity)
    else:
        return jsonify({"error": "product not found"}), 404


@app.route("/shirtmancity", methods=["POST"])
def create_shirtmancity():
    data = request.get_json()
    existing_shirtmancity = collections["collection2"].find_one({"shirtmancity_code": data["shirtmancity_code"]})
    if existing_shirtmancity:
        return jsonify({"error": "Shirt with the same product code already exists"}), 409
    else:
        collections["collection2"].insert_one(data)
        return jsonify({"message": "Shirt created successfully"}), 201

@app.route("/shirtmancity/<int:shirtmancity_id>", methods=["PUT"])
def update_shirtmancity(shirtmancity_id):
    data = request.get_json()
    existing_shirtmancity = collections["collection2"].find_one({"_id": shirtmancity_id})
    if existing_shirtmancity:
        collections["collection2"].update_one({"_id": shirtmancity_id}, {"$set": data})
        updated_shirtmancity = collections["collection2"].find_one({"_id": shirtmancity_id})
        return jsonify(updated_shirtmancity)
    else:
        return jsonify({"error": "shirt not found"}), 404
    
@app.route("/shirtmancity/<int:shirtmancity_id>", methods=["DELETE"])
def delete_shirtmancity(shirtmancity_id):
    result = collections["collection2"].delete_one({"_id": shirtmancity_id})
    if result.deleted_count:
        return jsonify({"message": "Shirt deleted successfully"}), 200
    else:
        return jsonify({"error": "Shirt not found"}), 404
    
# -------------------------------------------------------------------------------------------------------

@app.route("/shirtLiver", methods=["GET"])
def get_all_shirtLiver():
    shirtLiver = list(collections["collection3"].find())
    return jsonify(shirtLiver)

@app.route("/shirtLiver/<int:shirtLiver_id>", methods=["GET"])
def get_shirtLiver(shirtLiver_id):
    shirtLiver = collections["collection3"].find_one({"_id": shirtLiver_id})
    if shirtLiver:
        return jsonify(shirtLiver)
    else:
        return jsonify({"error": "product not found"}), 404


@app.route("/shirtLiver", methods=["POST"])
def create_shirtLiver():
    data = request.get_json()
    existing_shirtLiver = collections["collection3"].find_one({"shirtLiver_code": data["shirtLiver_code"]})
    if existing_shirtLiver:
        return jsonify({"error": "Shirt with the same product code already exists"}), 409
    else:
        collections["collection3"].insert_one(data)
        return jsonify({"message": "Shirt created successfully"}), 201

@app.route("/shirtLiver/<int:shirtLiver_id>", methods=["PUT"])
def update_shirtLiver(shirtLiver_id):
    data = request.get_json()
    existing_shirtLiver = collections["collection3"].find_one({"_id": shirtLiver_id})
    if existing_shirtLiver:
        collections["collection3"].update_one({"_id": shirtLiver_id}, {"$set": data})
        updated_shirtLiver = collections["collection3"].find_one({"_id": shirtLiver_id})
        return jsonify(updated_shirtLiver)
    else:
        return jsonify({"error": "shirt not found"}), 404
    
@app.route("/shirtLiver/<int:shirtLiver_id>", methods=["DELETE"])
def delete_shirtLiver(shirtLiver_id):
    result = collections["collection3"].delete_one({"_id": shirtLiver_id})
    if result.deleted_count:
        return jsonify({"message": "Shirt deleted successfully"}), 200
    else:
        return jsonify({"error": "Shirt not found"}), 404
    
# ------------------------------------------------------------------------------------------------------- 

@app.route("/shirtarsenal", methods=["GET"])
def get_all_shirtarsenal():
    shirtarsenal = list(collections["collection4"].find())
    return jsonify(shirtarsenal)

@app.route("/shirtarsenal/<int:shirtarsenal_id>", methods=["GET"])
def get_shirtarsenal(shirtarsenal_id):
    shirtarsenal = collections["collection4"].find_one({"_id": shirtarsenal_id})
    if shirtarsenal:
        return jsonify(shirtarsenal)
    else:
        return jsonify({"error": "product not found"}), 404


@app.route("/shirtarsenal", methods=["POST"])
def create_shirtarsenal():
    data = request.get_json()
    existing_shirtarsenal = collections["collection4"].find_one({"shirtarsenal_code": data["shirtarsenal_code"]})
    if existing_shirtarsenal:
        return jsonify({"error": "Shirt with the same product code already exists"}), 409
    else:
        collections["collection4"].insert_one(data)
        return jsonify({"message": "Shirt created successfully"}), 201

@app.route("/shirtarsenal/<int:shirtarsenal_id>", methods=["PUT"])
def update_shirtarsenal(shirtarsenal_id):
    data = request.get_json()
    existing_shirtarsenal = collections["collection4"].find_one({"_id": shirtarsenal_id})
    if existing_shirtarsenal:
        collections["collection4"].update_one({"_id": shirtarsenal_id}, {"$set": data})
        updated_shirtarsenal = collections["collection4"].find_one({"_id": shirtarsenal_id})
        return jsonify(updated_shirtarsenal)
    else:
        return jsonify({"error": "shirt not found"}), 404
    
@app.route("/shirtarsenal/<int:shirtarsenal_id>", methods=["DELETE"])
def delete_shirtarsenal(shirtarsenal_id):
    result = collections["collection4"].delete_one({"_id": shirtarsenal_id})
    if result.deleted_count:
        return jsonify({"message": "Shirt deleted successfully"}), 200
    else:
        return jsonify({"error": "Shirt not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# vofrhuh