from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    service_type_id = Column(Integer, ForeignKey("service_type.id"))

    service_type = relationship("ServiceType", back_populates="service")

    def __init__(self, name, service_type_id):
        self.name = name
        self.service_type_id = service_type_id