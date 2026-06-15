import uuid

from datetime import datetime

from enum import Enum

from pydantic import BaseModel

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class CustomerRole(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class CustomerSchema(BaseModel):
    id: str
    name: str
    email: str
    role: CustomerRole
    tenant_id: str
    created_at: datetime
    modified_at: datetime

    model_config = {
        "from_attributes": True
    }

class Customer(Base):
    __tablename__ = "customers"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)
    tenant_id = Column(String(36), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    modified_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())