"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    try:
    # this is how you can use the Family datastructure by calling its methods
        members = jackson_family.get_all_members()        
        if members == []:
            return jsonify({"msg":"No members found"}),404
        else : return jsonify(members), 200
    
    except Exception as err:
        return jsonify({"error":"Internal Server Error","message":str(err)}),500



@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    try:        
        member = jackson_family.get_member(id)
        if member is None:
            return  jsonify({"msg":"No member found"}),404
        else : return jsonify(member),200        

    except Exception as err:
        return jsonify({"error":"Internal Server Error","message":str(err)}),500
@app.route('/member', methods=['POST'])
def new_member():
    
    try:
        body = request.get_json(force=True)
        new_id = jackson_family._generate_id()
        body["id"] = new_id        
        jackson_family.add_member(body)
        return jsonify(body)
    except Exception as err:
        return jsonify({"error":"Internal Server Error", "message":str(err)}),500

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member is None:
            return jsonify({"msg":"Member not found, nothing to delete"}),404
        else: 
            jackson_family.delete_member(member_id)
            return jsonify({"done":"true"})
    except Exception as err:
        return jsonify({"eroor":"Internal Server Error","message":str(err)}),500
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
