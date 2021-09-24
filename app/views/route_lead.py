from flask import Blueprint, request, jsonify 
from app.models.lead_model import LeadModel
from app.models.user_exceptions import ErrPhoneFormat
from app.controllers.lead_controller import list_leads,format_fone,update_lead,delete_lead
from datetime import  datetime
import sqlalchemy
from app.configs.database import db 

bp_lead = Blueprint('leads', __name__, url_prefix='/api')

@bp_lead.route('/lead',methods = ['POST'])
def post_add_person_vaccinated():
        
        try :
                data = request.get_json()
                is_correct = format_fone(data)
                
                if is_correct :
                        
                        today = datetime.utcnow()
                        new_lead =  LeadModel( 
                                name = data["name"],
                                email = data["email"],
                                phone = data["phone"],
                                create_date = today,
                                last_visit = today                   
                                )
                        
                        from app.configs.database import db 
                      
                        db.session.add(new_lead)
                       
                        db.session.commit()
                        
                        return jsonify(new_lead.to_json()),201
                
                raise ErrPhoneFormat()
        
        except  ErrPhoneFormat as err:
                return err.message,401
        
        except sqlalchemy.exc.IntegrityError:
                return {"Value exists":"The email or name data already exists in the database "},401
         
@bp_lead.route('/lead',methods = ['GET'])
def get_all_vaccinated():
       
        query = list_leads()
        if len(list(query)) == 0 :
                return {"Error":"Database is empty"},404
        return jsonify(query),202


@bp_lead.route('/lead',methods = ['PATCH'])
def upgrade_lead(): 
        data = request.get_json()
        try :
                if len(list(data)) == 1 and  data['email'] :
                        email = data['email']
                        make_update = update_lead(email)
                        if make_update :
                                return "",201
                        
                        return {"Error":"no data found "},403
                
                return {"Error":"only accept email field"},404
        
        except KeyError :
                return {"Error":"the email field is spelled wrong or does not exist "},404

@bp_lead.route('/lead',methods = ['DELETE'])
def delete(): 
        data = request.get_json()
        try :
                if len(list(data)) == 1 and  data['email'] :
                        email = data['email']
                        print(email)
                        make_delete = delete_lead(email)
                        if make_delete :
                                return "",201
                        
                        return {"Error":"no data found "},403
                
                return {"Error":"only accept email field"},404
        
        except KeyError :
                
                return {"Error":"the email field is spelled wrong or does not exist "},404
        