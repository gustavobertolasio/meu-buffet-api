from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Brand(Base):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)

    unit = relationship("Unit", back_populates="brand")

    def __init__(self, name, cnpj):
        self.name = name
        self.cnpj = cnpj
