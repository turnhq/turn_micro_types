from typing import TypedDict


class DecodedServerSideToken(TypedDict):
    """
    Decoded server side tokens from Auth0 will
    return a dictionary with the following keys.
    """

    iss: str
    sub: str
    aud: str
    iat: int
    exp: int
    azp: str
    scope: str  # This is a space separated string of scopes
    gty: str
