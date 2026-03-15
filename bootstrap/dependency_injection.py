from typing import Dict, Callable, List

from adapters import *
from domain.models import *
from proxy_pool import *
from http_engine import *
from http_parser import *

from lagom import Container


def create_adapter_deps(container: Container) -> None:
    container[AbstractHttpAdapter] = PlainHttpAdapter


def create_proxy_pool_deps(container: Container) -> None:
    container[FreeProxyCollector] = FreeProxyCollector
    container[PrivateProxyCollector] = PrivateProxyCollector

    container[Dict[ProxyType, AbstractProxyCollectorMethod]] = {
        ProxyType.FREE: container[FreeProxyCollector],
        ProxyType.PRIVATE: container[PrivateProxyCollector]
    }

    container[AbstractProxyCollectorService] = ProxyCollectorService
    container[AbstractProxyQualityService] = ProxyQualityService()

    container[AbstractProxyPoolClient] = ProxyPoolClient(
        container[AbstractProxyCollectorService], container[AbstractProxyQualityService]
    )


def create_http_engine_deps(container: Container) -> None:
    container[AbstractProxyHttpRequestService] = ProxyHttpRequestService
    container[AbstractBatchHttpProxyService] = BatchHttpProxyService
    container[AbstractHttpRequestService] = HttpRequestService
    container[AbstractHttpEngineClient] = HttpEngineClient


def create_http_parser_deps(container: Container) -> None:
    container[List[AbstractNestedParser]] = []

    container[List[AbstractResponseParser]] = [
        JavascriptJsonParser()
    ]

    container[AbstractFlattenerService] = FlattenerService
    container[AbstractObjectMatcherService] = ObjectMatcherService
    container[AbstractDataItemExtractorService] = DataItemExtractorService
    container[AbstractParserService] = ParserService
    container[AbstractHttpParserClient] = HttpParserClient


def create_di_container() -> Container:
    dep_order_list: List[Callable] = [
        create_adapter_deps,
        create_proxy_pool_deps,
        create_http_parser_deps,
        create_http_engine_deps
    ]

    di_container = Container()

    for dep_setter in dep_order_list:
        dep_setter(di_container)

    return di_container
