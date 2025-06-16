from pydantic import BaseModel


class CreateBrandSchema(BaseModel):
    name: str
    cnpj: str

    class Config:
        from_attributes = True
