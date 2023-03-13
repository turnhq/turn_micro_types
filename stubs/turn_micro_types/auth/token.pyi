from typing import TypedDict

class DecodedServerSideToken(TypedDict):
    iss: str
    sub: str
    aud: str
    iat: int
    exp: int
    azp: str
    scope: str
    gty: str
