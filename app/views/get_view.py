from app.model.creationLead import CreationLead
from flask import jsonify, Blueprint

def get_view():
    data = CreationLead.get()
    return jsonify(data)