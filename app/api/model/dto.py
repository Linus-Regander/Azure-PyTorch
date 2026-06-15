from pydantic import BaseModel

from app.api.model.model import CustomerSchema

class CustomerRequest(BaseModel):
    """
    Request model for persisting customers in the database.
    """
    
    name: str
    email: str
    role: str
    tenant_id: str

class CustomerResponse(BaseModel):
    """
    Response model for returning customers from the database.
    """
    
    customers: list[CustomerSchema]
    count: int