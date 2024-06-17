from typing import Dict, Optional

from pydantic import BaseModel


class AiResponse(BaseModel):
    disposition: Optional[str] = None
    plea: Optional[str] = None
    status: Optional[str] = None
    model: Optional[str] = None
    prompt: Optional[str] = None


class ClassificationDataAttributes(BaseModel):
    classification: str
    source: str
    ai_response: Optional[AiResponse] = None


class ClassificationData(BaseModel):
    description: str
    classification_data: ClassificationDataAttributes


class ClassificationResponse(BaseModel):
    success: bool
    data: ClassificationData


class ClassificationDictResponse(BaseModel):
    success: bool
    data: Dict[str, ClassificationDataAttributes]
