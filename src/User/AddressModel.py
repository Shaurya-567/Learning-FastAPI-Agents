from pydantic import BaseModel, Field

class AddressModel(BaseModel):
    street: str = Field(..., description="The street address")
    city: str = Field(..., description="The city of the address")
    state: str = Field(..., description="The state of the address")
    zip_code: str = Field(..., description="The ZIP code of the address")

    class Config:
        schema_extra = {
            "example": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip_code": "12345"
            }
        }