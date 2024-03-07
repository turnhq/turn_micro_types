from pydantic import BaseModel


class CreateOrderRequestBody(BaseModel):
    worker_id: str
    recheck_id: str | None
