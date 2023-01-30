from flask import Blueprint, jsonify, request
from BLL.members_bl import MembersBL

members_bl = MembersBL()
members = Blueprint('members', __name__)


#! GET
@members.route('/', methods=['GET'])
def get_all_members():
    members = members_bl.get_all_members()
    return jsonify(members)


#! GET by id
@members.route("/<id>", methods=['GET'])
def get_member(id):
    member = members_bl.get_member(id)
    return jsonify(member)


#! POST
@members.route('/', methods=['POST'])
def add_member():
    obj = request.json
    member = members_bl.add_member(obj)
    return jsonify(member)


#! put
@members.route('/<id>', methods=['PUT'])
def update_member(id):
    obj = {"name": request.json["name"],
           "email": request.json["email"], "city": request.json["city"]}
    member = members_bl.update_member(id, obj)
    return jsonify(member)


#! DELETE
@members.route('/<id>', methods=['DELETE'])
def delete_member(id):
    member = members_bl.delete_member(id)
    return jsonify(member)
