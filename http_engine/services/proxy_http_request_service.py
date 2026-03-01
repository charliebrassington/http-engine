from adapters import HttpResponse, AbstractHttpAdapter
from http_engine import HttpEngineRequest
from http_engine.interfaces import AbstractProxyHttpRequestService
from proxy_pool import AbstractProxyPoolClient


class ProxyHttpRequestService(AbstractProxyHttpRequestService):
    def __init__(self, http_adapter: AbstractHttpAdapter, proxy_pool_client: AbstractProxyPoolClient) -> None:
        self._http_adapter = http_adapter
        self._proxy_pool_client = proxy_pool_client

    def send_proxied_http_request(self, engine_request: HttpEngineRequest) -> HttpResponse:
        proxy = self._proxy_pool_client.get_proxy()
        response = self._http_adapter.make_request(method=engine_request.method, url=engine_request.url, proxies={"https": f"http://{proxy}"}, timeout=5)

        self._proxy_pool_client.update_proxy_quality(proxy=proxy, success=response.success)

        return response
