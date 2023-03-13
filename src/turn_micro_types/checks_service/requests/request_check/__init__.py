from pydantic import BaseModel


class RequestCheckSchema(BaseModel):
    partner_worker_id: int
    package_id: int
