from enum import Enum


class SupportEmailCommunicationCategory(str, Enum):
    PRE_ADVERSE_NOTICE = "Pre-Adverse Notice"
    ADVERSE_ACTION_NOTICE = "Adverse Action Notice"
    COMPLICANCE_REVIEW = "Compliance review"
    COMPLIANCE_REVIEW_SEX_OFFENDER = "Compliance review Sex Offender"
    RECORDS_AUDIT_LAST_NAME = "Records Audit: Last Name"
