from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class ServiceType(Base):
    __tablename__ = "service_type"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)


    service = relationship("Service", back_populates="service_type")

    def __init__(self, name):
        self.name = name