from http_engine.interfaces import AbstractHttpEngineClient, AbstractHttpRequestService, AbstractBatchHttpProxyService
from http_engine.models import HttpEngineRequest, HttpEngineResponse


class HttpEngineClient(AbstractHttpEngineClient):
    def __init__(
        self,
        http_request_service: AbstractHttpRequestService,
        batch_http_proxy_service: AbstractBatchHttpProxyService
    ) -> None:
        self._http_request_service = http_request_service
        self._batch_http_proxy_service = batch_http_proxy_service

    def send_http_request(self, http_request: HttpEngineRequest) -> HttpEngineResponse:
        if http_request.proxy_pool_enabled:
            http_response = self._batch_http_proxy_service.send_batched_http_request(http_request)
        else:
            http_response = self._http_request_service.send_http_request(http_request)

        return HttpEngineResponse(success=True, data_wanted={"test": http_response.raw_text})
