def is_type_correct(data):
    if type(data["email"]) != str:
        return False
    else:
        return True


def lost_parameters(data): 
    if "email" in data.keys():
        return True
    else:
        return {"error": "a unica chave que tem que ser passada é o email"}