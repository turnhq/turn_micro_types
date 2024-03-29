from datetime import date, datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl

from turn_micro_types.worker_micro.responses.PartnerWorker.responses.partner_worker_document import (  # noqa: E501
    PartnerWorkerDocumentEntry,
)


class PartnerWorkerAddressSchema(BaseModel):
    id: Optional[UUID] = None
    is_current_address: Optional[bool] = None
    is_added_manually: Optional[bool] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    county: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    zip: Optional[str] = None
    zip4: Optional[str] = None
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    report_token: Optional[str] = None
    search_result_uuid: Optional[UUID] = None
    hash: Optional[str] = None
    create_timestamp: Optional[datetime] = None
    tlo_order: Optional[int] = None
    fips: Optional[int] = None


class PartnerWorkerDetailsSchema(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    mother_maiden_name: Optional[str] = None
    address: Optional[PartnerWorkerAddressSchema] = None
    date_of_birth: Optional[date] = None
    package_id: Optional[str] = None
    uuid: Optional[UUID] = None
    worker_id: Optional[UUID] = None
    candidate_consent_email_id: Optional[str] = None
    signature_img: Optional[str] = None
    partner_id: int
    partner_name: str
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
    drivers_license_front_image_url: Optional[HttpUrl] = None
    drivers_license_expiration_date: Optional[date] = None
    partner_worker_id_document_url: Optional[HttpUrl] = None
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
    turn_id: str
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
