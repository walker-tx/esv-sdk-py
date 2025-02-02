from ..types import BeforeRequestHook, BeforeRequestContext
import httpx
from typing import Union


class PrefixApiKeyHook(BeforeRequestHook):
    prefix = "Token"

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        existing_token: str = request.headers.get("Authorization")

        if existing_token.startswith(self.prefix):
            return request

        request.headers["Authorization"] = f"{self.prefix} {existing_token}"

        return request
