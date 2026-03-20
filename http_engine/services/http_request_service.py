from adapters import HttpResponse, AbstractHttpAdapter
from http_engine import HttpEngineRequest
from http_engine.interfaces import AbstractHttpRequestService


class HttpRequestService(AbstractHttpRequestService):
    def __init__(self, http_adapter: AbstractHttpAdapter) -> None:
        self._http_adapter = http_adapter

    def send_http_request(self, engine_request: HttpEngineRequest, **kwargs) -> HttpResponse:
        return self._http_adapter.make_request(method=engine_request.method, url=engine_request.url, **kwargs)
