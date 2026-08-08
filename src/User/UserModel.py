from pydantic import BaseModel, Field
from src.User.AddressModel import AddressModel

class UserModel(BaseModel):
    id: int = Field(..., description="The unique identifier for the user")
    firstName: str = Field(..., description="The user's first name")
    maidenName: str = Field(..., description="The user's maiden name")
    lastName: str = Field(..., description="The user's last name")
    email: str = Field(..., description="The user's email address")
    address: AddressModel = Field(..., description="The user's address")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "firstName": "John",
                "maidenName": "Doe",
                "lastName": "Smith",
                "email": "john.smith@example.com",
                "address": {
                    "street": "123 Main St",
                    "city": "Anytown",
                    "state": "CA",
                    "zip_code": "12345"
                }
            }
        }