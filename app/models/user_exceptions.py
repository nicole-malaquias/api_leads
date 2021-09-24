class FieldError(Exception):
    def __init__(self, data):
        
        data = list(data)
        problem = [ i for i in data if i not in ["name","email","phone"] ]
        
        self.message = {
            "available_keys": [
                "name", "email","phone",
                ],
            "Wrong_keys_sended": [*problem]          
        }
        super().__init__(self.message)


class ErrPhoneFormat(Exception):
    
    def __init__(self):
        
        
        self.message = {
            "invalid format": "the phone field format is wrong."    
        }
        super().__init__(self.message)

