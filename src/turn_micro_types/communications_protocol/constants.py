from enum import Enum


class SupportEmailCommunicationCategory(str, Enum):
    PRE_ADVERSE_NOTICE = "Pre-Adverse Notice"
    ADVERSE_ACTION_NOTICE = "Adverse Action Notice"
    COMPLICANCE_REVIEW = "Compliance review"
    COMPLIANCE_REVIEW_SEX_OFFENDER = "Compliance review Sex Offender"
    RECORDS_AUDIT_LAST_NAME = "Records Audit: Last Name"
    FAILED_TO_REQUEST_COUNTY_CHECK = "Failed to request county check"
    FEDERAL_CHECK_DISTRICT_NOT_FOUND = "Federal check district not found"
    MANUAL_BACKGROUND_CHECK = "Manual background check"
    WSS_ATTENTION = "WSS attention"
    WSS_FEDERAL_ATTENTION = "WSS federal attention"
    PARTNER_WORKER_REVIEW = "Partner Worker Review"
