from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class PartnerWorkerDetailsSchema(BaseModel):
    id: int
    uuid: Optional[UUID]
    worker_id: Optional[UUID]
    candidate_consent_email_id: Optional[str]
    partner_id: int
    worker_consent: Optional[bool]
    worker_assent: Optional[bool]
    finish_review: Optional[bool]
    profile_status: Optional[str]
    note: Optional[str]
    updated_by: Optional[str]
    is_ssn_valid: Optional[int]
    is_ssn_deceased: Optional[int]
    is_ssn_random: Optional[int]
    drivers_license_state: Optional[str]
    drivers_license_number: Optional[str]
    zipcode: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    create_timestamp: Optional[datetime]
    intuit_id: Optional[int]
    is_county_criminal_report_updated: Optional[bool]
    fountain_id: Optional[UUID]
    is_manual_background_check: Optional[bool]
    manual_background_check_report_url: Optional[str]
    is_mvr_report_updated: Optional[bool]
    reference_id: Optional[str]
    turn_id: Optional[str]
    workflow_turn_id: Optional[str]
    workflow_package_id: Optional[str]
    check_status: Optional[str]
    consent_date: Optional[datetime]
    sms_opt_in: Optional[bool]
    full_name: str
    completion_date: Optional[datetime]
    city: Optional[str]
    state: Optional[str]
