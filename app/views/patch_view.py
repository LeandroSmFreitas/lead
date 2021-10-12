from flask import request, Blueprint
from app.controller.Patch_delete import is_type_correct, lost_parameters
from app.model.creationLead import CreationLead
from app.configs.database import db

def patch_view():
    data = request.get_json()

    parameters = lost_parameters(data)
    if parameters != True:
        return parameters

    is_correct = is_type_correct(data)
    if not is_correct:
        return {"error": "os tipo da chave deve ser string"}

    query = CreationLead.patch(data)

    if not query: 
        return {"error": "cadastro não encontrado"}

    db.session.add(query)
    db.session.commit()

    return {}


