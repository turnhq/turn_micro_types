from turn_micro_types.turn_state_machine import StateMachineOptions


class PARTNER_WORKER_STATES(StateMachineOptions):
    INITIATED = "initiated"
    PENDING = "pending"
    CONSENT = "consent"
    EMAILED = "emailed"
    APPROVED = "approved"
    REJECTED = "rejected"
    PROCESSING = "processing"
    FIRST_NOTICE = "pending__first_notice"
    SECOND_NOTICE = "pending__second_notice"
    RESOLVED = "pending__resolved"
    DISPUTE = "pending__dispute"
    REVIEW = "review"
    WITHDRAWN = "withdrawn"
    SSN_TRACE_FAILED = "review__identity"
    MVR_FAILED = "review__mvr"
    COMPLIANCE = "review__qa"
    REVIEW_SEX_OFFENDER = "review__so"
