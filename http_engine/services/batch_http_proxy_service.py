from typing import List
from threading import Thread

from adapters import HttpResponse
from http_engine.models import HttpEngineRequest
from http_engine.interfaces import AbstractProxyHttpRequestService, AbstractBatchHttpProxyService
from core.multi_threading import run_threads


class BatchHttpProxyService(AbstractBatchHttpProxyService):
    def __init__(self, proxy_http_request_service: AbstractProxyHttpRequestService) -> None:
        self._proxy_http_request_service = proxy_http_request_service

    def threaded_proxied_http_request(self, engine_request: HttpEngineRequest, responses: List[HttpResponse]) -> None:
        responses.append(self._proxy_http_request_service.send_proxied_http_request(engine_request))

    def send_batched_http_request(self, engine_request: HttpEngineRequest, batch_amount: int = 10) -> HttpResponse:
        batch_responses = []
        while True:
            run_threads(thread_list=[
                Thread(target=self.threaded_proxied_http_request, args=(engine_request, batch_responses))
                for _ in range(batch_amount)
            ])

            if batch_successes := [response for response in batch_responses if response.success]:
                return batch_successes[0]
