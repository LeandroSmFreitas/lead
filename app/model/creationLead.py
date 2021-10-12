from app.configs.database import db
from app.model.leads_model import LeadsModel
from datetime import datetime


class CreationLead: 
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone

    @staticmethod
    def get():
        data = LeadsModel.query.order_by(-LeadsModel.visits).all()
        if data == None:
            return {}
        
        return data

    @staticmethod
    def patch(data):
        query = LeadsModel.query.filter_by(email=data["email"]).first()

        if query == None:
            return False

        visits = query.visits
        last_visit = query.last_visit

        visits = visits + 1
        last_visit = datetime.now()

        new_date = {
            "visits": visits,
            "last_visit": last_visit
        }

        for key, value in new_date.items():
            setattr(query, key, value)

        return query

    @staticmethod
    def delete(data):
        query = LeadsModel.query.filter_by(email=data["email"]).first()
        db.session.delete(query)
        db.session.commit()

    def save(self):
        new_lead = LeadsModel(
            name= self.name,
            email= self.email,
            phone= self.phone,
            creation_date= datetime.now(),
            last_visit= datetime.now(),
        )
        return new_lead