from typing import cast
import jwt
from turn_micro_types.auth.token import DecodedServerSideToken


class InternalAuthService:
    """
    Class to handle authentication for internal users.
    To be imported into different microservices to handle authentication.

    Should be initiated with the relevant PUBLIC_KEY for the Auth0 tenant
    which is being used.
    """

    __slots__ = ("public_key", "audience")

    public_key: str
    audience: str

    def __init__(self, public_key: str, audience: str) -> None:
        self.public_key = public_key
        self.audience = audience

    def authenticate(self, token: str) -> DecodedServerSideToken:
        """
        Authenticate a token from an internal user.

        :param token: The token to be authenticated.
        :return: The decoded token.
        """
        decoded = jwt.decode(
            token,
            self.public_key,
            algorithms=["RS256"],
            audience="https://turner-internal.auth0.com/api/v2/",
        )
        return cast(DecodedServerSideToken, decoded)
