from typing import List, Dict

from domain.models import ProxyPoolConfig, ProxyType

from adapters import AbstractHttpAdapter

from proxy_pool.interfaces import AbstractProxyCollectorMethod, AbstractProxyCollectorService
from core.errors import ProxyPathNotSet


PROXY_URL_LIST = (
    "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=ipport&format=text",
    "https://proxylist.geonode.com/api/proxy-list?protocols=https%2Chttp&limit=500&page=1&sort_by=lastChecked&sort_type=desc",
    "https://vakhov.github.io/fresh-proxy-list/proxylist.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/https/data.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt",
    "https://raw.githubusercontent.com/Argh94/Proxy-List/refs/heads/main/HTTP.txt",
    "https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/http_proxies.txt",
    "https://raw.githubusercontent.com/elliottophellia/proxylist/refs/heads/master/results/http/global/http_checked.txt",
    "https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/https.txt"
)


class FreeProxyCollector(AbstractProxyCollectorMethod):
    def __init__(self, http_adapter: AbstractHttpAdapter):
        self._http_adapter = http_adapter

    def collect_proxies(self, proxy_path: str) -> List[str]:
        return list(set(
            proxy.replace("http://", "")
            for proxy_url in PROXY_URL_LIST
            for proxy in self._http_adapter.make_request(method="get", url=proxy_url).raw_text.splitlines()
        ))


class PrivateProxyCollector(AbstractProxyCollectorMethod):
    def collect_proxies(self, proxy_path: str) -> List[str]:
        if not proxy_path:
            raise ProxyPathNotSet("proxy path must be set within config for private proxies")

        with open(proxy_path) as proxy_file:
            return proxy_file.readlines()


class ProxyCollectorService(AbstractProxyCollectorService):
    def __init__(self, proxy_collector_method: Dict[ProxyType, AbstractProxyCollectorMethod]):
        self._proxy_collector_method = proxy_collector_method

    def collect_proxies(self, config: ProxyPoolConfig) -> List[str]:
        proxy_collector_method = self._proxy_collector_method[config.proxy_type]

        return proxy_collector_method.collect_proxies(proxy_path=config.proxy_path)
