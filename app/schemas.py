from pydantic import Basemodel, EmailStr 

class UserCreate(Basemodel): 
    email: EmailStr 
    
    class Config:
        from_atrributes = True 