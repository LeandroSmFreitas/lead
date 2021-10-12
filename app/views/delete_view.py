from flask import Blueprint,request
from app.controller.Patch_delete import is_type_correct, lost_parameters
from app.model.creationLead import CreationLead



def delete_view():
    data = request.get_json()
    
    parameters = lost_parameters(data)
    if parameters != True:
        return parameters
    
    is_correct = is_type_correct(data)
    if not is_correct:
        return {"error": "os tipo da chave deve ser string"}
    
    CreationLead.delete(data)

    return {}