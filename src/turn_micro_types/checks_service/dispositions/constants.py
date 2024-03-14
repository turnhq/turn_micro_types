import enum


class DispositionDescription(enum.Enum):
    DISMISSED = "DISMISSED"
    CONVICTED = "CONVICTED"
    NOT_GUILTY = "NOT GUILTY"
    DISPOSED = "DISPOSED"
    DEFERRED = "DEFERRED"
    GUILTY = "GUILTY"
    CONVICTION = "CONVICTION"
    DISMISSAL = "DISMISSAL"
    GUILTY_PLEA = "GUILTY PLEA"
    PENDING = "PENDING"
    NOLO = "NOLO"
    NOLLE = "NOLLE"


class DispositionClassification(enum.Enum):
    CONVICTION = "CONVICTION"
    NON_CONVICTION = "NON_CONVICTION"
    NOT_ENOUGH_INFORMATION = "NOT_ENOUGH_INFORMATION"
    PENDING = "PENDING"
