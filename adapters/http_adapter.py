from adapters.interfaces import AbstractHttpAdapter
from adapters.models import HttpResponse

import requests


class PlainHttpAdapter(AbstractHttpAdapter):
    def make_request(self, method: str, url: str, **kwargs) -> HttpResponse:
        response = requests.request(method=method, url=url, **kwargs)
        return HttpResponse(
            raw_text=response.text,
            status_code=response.status_code
        )
