
from datetime import  datetime
from app.configs.database import db
from app.models.lead_model import LeadModel 
import re

def list_leads():
    query = LeadModel.query.order_by(LeadModel.visits.desc()).all()
    return query

def format_fone(data):
    
    pattern ='\(\d{2,}\)\d{5,}\-\d{4}'
    phone = data['phone']
    query = re.fullmatch(pattern,phone)
    
    if query == None:
        return False 
    return True 

def update_lead(email):
    
    try :

        lead = LeadModel.query.filter_by(email = email).first()
        visits_update  = lead.visits + 1 
        lead.visits = visits_update
        lead.last_visit = datetime.utcnow()
        db.session.add(lead)
        db.session.commit()
        return True 
    except:
        return False    

def delete_lead(email):
    try :
        lead = LeadModel.query.filter_by(email = email).first()
        db.session.delete(lead)
        db.session.commit()
        return True
    except:
        return False