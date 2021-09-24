from sqlalchemy import Column,String, Integer,DateTime, select,Sequence
from dataclasses import dataclass
from app.configs.database import db


@dataclass
class LeadModel(db.Model):
    
    name : str
    email : str 
    phone : str 
    create_date : str 
    last_visit : str
    visits : int 
    
    __tablename__ = 'lead_table'
    
    id = Column(Integer,  primary_key=True)
    name =  Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    create_date = Column(DateTime)
    last_visit = Column(DateTime)
    visits = Column(Integer,default=1)

    
    def to_json(self):
        import time
        today = time.strftime(f'%a, %d  %b %Y %H:%M:%S %z ')
        return {
            
            "name":self.name, 
            "email": self.email, 
            "phone": self.phone, 
            "create_date": self.create_date, 
            "last_visit":self.last_visit,
            "visits": self.visits,
        }
    
    @staticmethod
    def get_all_by_visits():
        query = db.session.query(LeadModel).order_by(LeadModel.visits)
        return query

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @staticmethod
    # def ValidateFormate(data):
        
    #     import re
    #     pattern ='\(\d{2,}\)\d{5,}\-\d{4}'
    #     phone = data['phone']
    #     query = re.fullmatch(pattern,phone)
        
    #     if query == None:
    #         return False 
    #     return True
        
    


