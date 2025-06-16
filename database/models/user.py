from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False)
    unit_id = Column(Integer, ForeignKey("unit.id"))

    unit = relationship("Unit", back_populates="user")

    def __init__(self, name, document, unit_id):
        self.name = name
        self.document = document
        self.unit_id = unit_id
