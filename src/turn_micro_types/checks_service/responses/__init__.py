from typing import List
from pydantic import BaseModel

from turn_micro_types.checks_service.constants import CheckType


class RunChecksEndpointResponse(BaseModel):
    checks_run: List[CheckType] = []
    errors: List[str] = []
