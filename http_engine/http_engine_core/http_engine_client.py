from http_engine.http_engine_core.interfaces import AbstractHttpEngineClient, AbstractHttpRequestService, AbstractBatchHttpProxyService
from http_engine.http_engine_core.models import HttpEngineRequest, HttpEngineResponse

from http_engine.http_parser import AbstractHttpParserClient


class HttpEngineClient(AbstractHttpEngineClient):
    def __init__(
        self,
        http_request_service: AbstractHttpRequestService,
        batch_http_proxy_service: AbstractBatchHttpProxyService,
        http_parser_client: AbstractHttpParserClient
    ) -> None:
        self._http_request_service = http_request_service
        self._batch_http_proxy_service = batch_http_proxy_service
        self._http_parser_client = http_parser_client

    def send_http_request(self, http_request: HttpEngineRequest) -> HttpEngineResponse:
        if http_request.proxy_pool_enabled:
            http_response = self._batch_http_proxy_service.send_batched_http_request(http_request)
        else:
            http_response = self._http_request_service.send_http_request(http_request)

        parsed_result = self._http_parser_client.parse_response(
            response=http_response, data_items=http_request.wanted_data_items
        )

        return HttpEngineResponse(success=True, data_wanted=parsed_result)
