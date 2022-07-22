from pydantic import BaseModel, validator, HttpUrl, UUID4


class Data(BaseModel):
    productId: int
    productCount: int
    price: float
    title: str
    imageUrl: HttpUrl
    discountedPrice: float = None
    discountedPercent: float = None
    commercialTitle: str
    quantity: int
    isPreOrderProduct: str = None
    productStatus: int
    customerId: UUID4
    details: str = None
    discountType: int
    discountValue: int = None
    valueType: str = None
    categorySlug: str
    productSlug: str
    productOriginalSlug: str


class ProductDetail(BaseModel):
    data: list[Data]
    totalPrice: float
    quantityFailed: bool


