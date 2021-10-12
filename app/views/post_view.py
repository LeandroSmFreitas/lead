from flask import request,current_app, jsonify, Blueprint
from app.controller.Post import compared_with_regex, email_or_phone_exist, lost_parameters, is_type_correct
from app.model.creationLead import CreationLead
from app.views import bp

@bp.route('/lead', methods=['POST'])
def post():
    data = request.get_json()

    parameters = lost_parameters(data)
    if parameters != True:
        return parameters

    type_correct = is_type_correct(data)
    if not type_correct:
        return {"error": "todas as chaves devem ser uma string"}


    result_of_regex = compared_with_regex(data["phone"])
    if not result_of_regex:
        return {"error": "O telefone deve ser no formato (xx)xxxxx-xxxx"}

    exists = email_or_phone_exist(data["email"], data["phone"])
    if exists != False:
        return exists
    
    lead = CreationLead(data["name"], data["email"], data["phone"])
    lead = lead.save()

    session = current_app.db.session
    session.add(lead)
    session.commit()
    return jsonify(lead.phone)




