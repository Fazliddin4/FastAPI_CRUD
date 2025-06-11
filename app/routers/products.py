from fastapi import Response, HTTPException, APIRouter
from app.fake_db import products
from app.schemas import ProductIn, ProductOut

router=APIRouter(
    prefix="/products",
    tags=["product"]
)

@router.get("/")
async def get_products():
    return products

@router.get("/{product_id}/")
async def get_product(product_id: int):
    res_product: dict = None
    for product in products:
        if product["id"]==product_id:
            res_product=product
            break
    if not res_product:
        raise HTTPException( status_code=404)
    
    return res_product

@router.post("/create/", response_model=ProductOut)
async def create_product(product: ProductIn):
    res_product=product.model_dump()
    res_product.update({"id": len(products)+1})
    products.append(product.model_dump())
    return res_product

@router.put("/{product_id}/update/", response_model=ProductOut)
async def update_product(product_id: int, product_in: ProductIn):
    res_product: dict=None

    for product in products:
        if product["id"]==product_id:
            res_product=product
            break

    if not res_product:
        raise HTTPException(detail={"message": "product not found"}, status_code=404)
    res_product.update(product_in.model_dump())
    return res_product



@router.delete("/{product_id}/delete")
async def delete_product(product_id: int):
    for product in products:    
        if product["id"]==product_id:
            products.remove(product)
            return Response(status_code=204)
        else:
             return HTTPException(detail="product not found", status_code=404)