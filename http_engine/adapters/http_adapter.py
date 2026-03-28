from http_engine.adapters.interfaces import AbstractHttpAdapter
from http_engine.adapters.models import HttpResponse

import requests


class PlainHttpAdapter(AbstractHttpAdapter):
    def make_request(self, method: str, url: str, **kwargs) -> HttpResponse:
        try:
            response = requests.request(method=method, url=url, **kwargs)
        except requests.exceptions.RequestException:
            return HttpResponse(success=False)

        return HttpResponse(
            success=True,
            raw_text=response.text,
            status_code=response.status_code
        )
