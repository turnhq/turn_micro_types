from typing import List
from pydantic import BaseModel

from turn_micro_types.checks_service.constants import CheckType


class RunChecksEndpointResponse(BaseModel):
    checks_run: List[CheckType] = []
    errors: List[str] = []


class CaseData(BaseModel):
    scheduling_url: str
    expiration: str
    cases: List[str]


class CreateOrderResponse(BaseModel):
    success: str
    case_number: str
    drug_test_window_update: str
    case_data: CaseData | None


class CreateOrderResponseBody(BaseModel):
    worker_id: str
    case_number: str
    recheck_id: str | None
    expiration: str
    scheduling_url: str
