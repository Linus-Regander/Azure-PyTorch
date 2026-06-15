from fastapi import APIRouter
from app.api.handler.customer import customer_router
from app.api.handler.health import health_router

main_router = APIRouter()

main_router.include_router(customer_router, prefix="/customer", tags=["customer"])
main_router.include_router(health_router, prefix="/health", tags=["health"])