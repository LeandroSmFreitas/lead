import re

from app.model.leads_model import LeadsModel

def compared_with_regex(data):
    pattern = r'^\([1-9]{2}\)(?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$'
    result = re.fullmatch(pattern, data, flags=0)
    if result == None:
        return False
    else:
        return True


def lost_parameters(data):
    if "name" in data.keys() and "phone" in data.keys() and "email" in data.keys():
        return True
    else:
        return {"erro": "Esta faltando chaves na sua requisição"}

def is_type_correct(data):
    if type(data["name"]) != str or type(data["email"]) != str or type(data["phone"]) != str:
        return False
    else:
        return True
    

def email_or_phone_exist(email, phone):
    email_verify = LeadsModel.query.filter_by(email=email).first()
    phone_verify = LeadsModel.query.filter_by(email=phone).first()
    if email_verify == None:
        return {"error": "email já existe"}
    elif phone_verify == None:
        return {"error": "telefone já existe"}
    
    return False