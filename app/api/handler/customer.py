from fastapi import APIRouter, Depends

from app.api.service.service import Service

from app.api.model.dto import CustomerRequest
from app.api.repository.repository import CustomerRepository

from app.db.session import Database
from app.config.config import Config

database = Database(config=Config().db_config())

customer_router = APIRouter()

def _get_service(db=Depends(database.get_db)):
    return Service(repository=CustomerRepository(db=db))

@customer_router.get("/{customer_id}")
async def get_customer(customer_id: str, service: Service = Depends(_get_service)):
    return await service.get_customer(tenant_id="", customer_id=customer_id) # no tenant id for now, since auth is not implemented.

@customer_router.get("/")
async def get_customers(service: Service = Depends(_get_service)):
    return await service.get_customers(tenant_id="") # no tenant id for now, since auth is not implemented.

@customer_router.post("/")
async def insert_customer(customer_req: CustomerRequest, service: Service = Depends(_get_service),):
    await service.insert_customer(tenant_id="", customer_req=customer_req) # no tenant id for now, since auth is not implemented.

@customer_router.put("/{customer_id}")
async def update_customer(customer_id: str, customer_req: CustomerRequest, service: Service = Depends(_get_service)):
    return await service.update_customer(tenant_id="", customer_id=customer_id, customer_req=customer_req) # no tenant id for now, since auth is not implemented.

@customer_router.delete("/{customer_id}")
async def delete_customer(customer_id: str, service: Service = Depends(_get_service)):
    await service.delete_customer(tenant_id="", customer_id=customer_id) # no tenant id for now, since auth is not implemented.