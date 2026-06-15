from sqlalchemy.ext.asyncio.session import AsyncSession

from app.api.model.exception.exception import AppException
from app.api.model.model import Customer

class CustomerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def select_customer(self, customer_id: str) -> Customer | None:
        """
        Selects a customer from the database.
        """
        
        try:
            return await self.db.get(Customer, customer_id)
        except Exception as e:
            await self.db.rollback()

            raise AppException(message=f"Failed to select customer, error: {e}", status_code=500)  

    async def select_customers(self) -> list[Customer]:
        """
        Selects all customers from the database.
        """
        
        try:
            return await self.db.execute(self.db.query(Customer)).scalars().all()
        except Exception as e:
            await self.db.rollback()

            raise AppException(message=f"Failed to select customers, error: {e}", status_code=500)  

    async def insert_customer(self, customer: Customer) -> None:
        """
        Insert a new customer into the database.
        """
        
        try:
            await self.db.add(customer)
            await self.db.commit()
            await self.db.refresh(customer)
        except Exception as e:
            await self.db.rollback()
            
            raise AppException(message=f"Failed to create customer, error: {e}", status_code=500)

    async def update_customer(self, customer: Customer) -> None:        
        """
        Updates a customer in the database.
        """
        
        try:
            await self.db.commit()
            await self.db.refresh(customer)
        except Exception as e:
            await self.db.rollback()
            
            raise AppException(message=f"Failed to update customer, error: {e}", status_code=500)

    async def delete_customer(self, customer: Customer) -> None:
        """
        Deletes a customer from the database.
        """
        
        try:
            await self.db.delete(customer)
            await self.db.commit()
        except Exception as e:
            await self.db.rollback()
            
            raise AppException(message=f"Failed to delete customer, error: {e}", status_code=500)