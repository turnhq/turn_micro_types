from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class PartnerWorkerDocumentType(Enum):
    bgc_report = "bgc_report"
    consent = "consent"
    dl_back = "dl-back"
    dl_front = "dl-front"
    document_image = "document_image"
    pa_form = "pa_form"
    photo_id_back = "photo_id-back"
    photo_id_face = "photo_id-face"
    photo_id_front = "photo_id-front"
    preadverse = "preadverse"


class PartnerWorkerDocumentEntry(BaseModel):
    id: int
    doc_type: str
    doc_url: str
    created_at: datetime
