from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    brand_id = Column(Integer, ForeignKey("brand.id"))

    brand = relationship("Brand", back_populates="unit")
    user = relationship("User", back_populates="unit")

    def __init__(self, name, brand_id):
        self.name = name
        self.brand_id = brand_id