from datetime import date, datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field

from turn_micro_types.worker_micro.responses.PartnerWorker.responses.partner_worker_document import (  # noqa: E501
    PartnerWorkerDocumentEntry,
)


class PartnerWorkerDetailsSchema(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    package_id: Optional[str] = None
    uuid: Optional[UUID] = None
    worker_id: Optional[UUID] = None
    candidate_consent_email_id: Optional[str] = None
    partner_id: int
    worker_consent: Optional[bool] = False
    worker_assent: Optional[bool] = False
    finish_review: Optional[bool] = False
    profile_status: Optional[str] = None
    note: Optional[str] = None
    updated_by: Optional[str] = None
    is_ssn_valid: Optional[int] = None
    is_ssn_deceased: Optional[int] = None
    is_ssn_random: Optional[int] = None
    drivers_license_state: Optional[str] = None
    drivers_license_number: Optional[str] = None
    zipcode: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    create_timestamp: Optional[datetime] = None
    intuit_id: Optional[int] = None
    is_county_criminal_report_updated: Optional[bool] = False
    fountain_id: Optional[UUID] = None
    is_manual_background_check: Optional[bool] = False
    manual_background_check_report_url: Optional[str] = None
    is_mvr_report_updated: Optional[bool] = False
    reference_id: Optional[str] = None
    turn_id: Optional[str] = None
    workflow_turn_id: Optional[str] = None
    workflow_package_id: Optional[str] = None
    check_status: Optional[str] = None
    consent_date: Optional[datetime] = None
    sms_opt_in: Optional[bool] = False
    full_name: str
    completion_date: Optional[datetime] = None
    city: Optional[str] = None
    state: Optional[str] = None
    documents: List[PartnerWorkerDocumentEntry] = Field(default_factory=list)
    ssn: Optional[str] = None
