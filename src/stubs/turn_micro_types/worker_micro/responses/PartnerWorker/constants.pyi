from turn_micro_types.turn_state_machine import StateMachineOptions as StateMachineOptions

class PARTNER_WORKER_STATES(StateMachineOptions):
    INITIATED: str
    PENDING: str
    CONSENT: str
    EMAILED: str
    APPROVED: str
    REJECTED: str
    PROCESSING: str
    FIRST_NOTICE: str
    SECOND_NOTICE: str
    RESOLVED: str
    DISPUTE: str
    REVIEW: str
    WITHDRAWN: str
    SSN_TRACE_FAILED: str
    MVR_FAILED: str
    COMPLIANCE: str
