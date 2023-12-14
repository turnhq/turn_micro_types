from typing import List

from pydantic import BaseModel


class ClassificationDictRequest(BaseModel):
    data: List[str]
