from typing import List, Optional

from pydantic import BaseModel


class ClassificationDictRequest(BaseModel):
    data: List[str]
    ai_enabled: Optional[bool]
    override_cache: Optional[bool]
