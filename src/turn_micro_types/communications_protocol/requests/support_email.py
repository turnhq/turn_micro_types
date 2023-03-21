from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from turn_micro_types.communications_protocol.constants import (
    SupportEmailCommunicationCategory,
)


class InternalCommsReferencesPWPayload(BaseModel):
    pw_id: int
    pw_uuid: UUID
    turn_id: str
    partner_id: int
    partner_name: str
    comm_type: SupportEmailCommunicationCategory
    support_email: Optional[str] = None
    info_for_agent: Optional[str] = None
