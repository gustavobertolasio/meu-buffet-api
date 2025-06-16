from fastapi import APIRouter, Depends, HTTPException
from database.session import get_session
from database.models.brand import Brand
from schemas.brand import CreateBrandSchema
from sqlalchemy.orm import Session
from utils import response


router = APIRouter(prefix="/brand", tags=["brand"])


@router.get("/")
async def get_all_brands(session=Depends(get_session)):
    brands = session.query(Brand).all()

    if len(brands):
        return brands
    else:
        return []


@router.post("/brand")
async def create_new_brand(
    schema: CreateBrandSchema, session: Session = Depends(get_session)
):
    brand = session.query(Brand).filter(Brand.cnpj == schema.cnpj).first()

    if brand:
        return HTTPException(status_code=400, detail="Marca ja cadastrada")
    else:
        new_brand = Brand(schema.name, schema.cnpj)
        session.add(new_brand)
        session.commit()

    return response("Marca criada com sucesso")


@router.get("/:id/unit")
async def get_all_brand_units():
    return {"Hello": "World"}
