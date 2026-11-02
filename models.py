from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    username:str
    password:str


    @validator('password')
    def validate_passwords(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one uppercase letter')
        return value 
        