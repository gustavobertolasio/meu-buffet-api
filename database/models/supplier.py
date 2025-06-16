from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    supplier_type_id = Column(Integer, ForeignKey("supplier_type.id"))

    supplier_type = relationship("SupplierType", back_populates="supplier")

    def __init__(self, name, supplier_type_id):
        self.name = name
        self.supplier_type_id = supplier_type_id