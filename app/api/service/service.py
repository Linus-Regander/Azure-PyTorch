from app.api.model.model import Customer, CustomerSchema
from app.api.repository.repository import CustomerRepository
from app.api.model.dto import CustomerRequest, CustomerResponse
from app.api.model.exception.exception import AppException

class Service():
    def __init__(self, repository: CustomerRepository):
        self.repository = repository
    
    async def get_customer(self, tenant_id: str, customer_id: str) -> CustomerSchema:
        if not tenant_id or not customer_id:
            raise AppException(message="Required request parameter is missing.", status_code=400)
        
        customer = await self.repository.get_customer(customer_id=customer_id)
        if not customer:
            raise AppException(message=f"Customer with ID {customer_id} not found.", status_code=404)

        return CustomerSchema.model_validate(customer)
    
    async def get_customers(self, tenant_id: str) -> CustomerResponse:
        if not tenant_id:
            raise AppException(message="Required request parameter is missing.", status_code=400)

        customers = await self.repository.select_customers()

        return CustomerResponse(customers=[CustomerSchema.model_validate(customer) for customer in customers], count=len(customers))
    
    async def insert_customer(self, tenant_id: str, customer_req: CustomerRequest):
        if not tenant_id:
            raise AppException(message="Required request parameter is missing.", status_code=400)
        
        if not customer_req:
            raise AppException(message="Required request body is missing.", status_code=400)
    
        customer = CustomerSchema(**customer_req.model_dump())

        await self.repository.insert_customer(customer=customer)
    
    async def update_customer(self, tenant_id: str, customer_id: str, customer_req: CustomerRequest):
        if not tenant_id or not customer_id:
            raise AppException(message="Required request parameter is missing.", status_code=400)
        
        customer = await self.repository.select_customer(customer_id=customer_id)
        if not customer:
            raise AppException(message=f"Customer with ID {customer_id} not found.", status_code=404)
        
        if customer.tenant_id != tenant_id:
            raise AppException(message="Unauthenticated access to customer", status_code=403)

        for key, value in customer_req.model_dump(exclude_unset=True).items():
            setattr(customer, key, value)

        await self.repository.update_customer(customer=customer)
    
    async def delete_customer(self, tenant_id: str, customer_id: str):
        if not tenant_id or not customer_id:
            raise AppException(message="Required request parameter is missing.", status_code=400)
        
        customer = await self.repository.select_customer(customer_id=customer_id)
        if not customer:
            raise AppException(message=f"Customer with ID {customer_id} not found.", status_code=404)
        
        if customer.tenant_id != tenant_id:
            raise AppException(message="Unauthenticated access to customer", status_code=403)
        
        await self.repository.delete_customer(customer=customer)