from typing import Dict

from pydantic import BaseModel


class ClassificationDataAttributes(BaseModel):
    similarity: str
    description: str


class ClassificationResponse(BaseModel):
    success: bool
    data: ClassificationDataAttributes


class ClassificationDictResponse(BaseModel):
    success: bool
    data: Dict[str, str]
