from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, StrictInt, StrictStr
from turn_micro_types.communications_protocol.constants import (
    SupportEmailCommunicationCategory,
)


class InternalCommsReferencesPWPayload(BaseModel):
    pw_id: StrictInt
    pw_uuid: UUID
    turn_id: str = Field(regex="^C\\d{10}$")
    partner_id: StrictInt
    partner_name: StrictStr
    comm_type: SupportEmailCommunicationCategory
    support_email: Optional[EmailStr] = None
    info_for_agent: Optional[StrictStr] = None
