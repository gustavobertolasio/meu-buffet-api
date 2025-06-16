from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class SupplierType(Base):
    __tablename__ = "supplier_type"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

    supplier = relationship("Supplier", back_populates="supplier_type")

    def __init__(self, name):
        self.name = name