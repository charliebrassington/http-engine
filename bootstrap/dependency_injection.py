from typing import Dict, Callable, List

from adapters import *
from domain.models import *
from proxy_pool import *

from lagom import Container


def create_adapter_deps(container: Container):
    container[AbstractHttpAdapter] = PlainHttpAdapter


def create_proxy_pool_deps(container: Container):
    container[FreeProxyCollector] = FreeProxyCollector
    container[PrivateProxyCollector] = PrivateProxyCollector

    container[Dict[ProxyType, AbstractProxyCollectorMethod]] = {
        ProxyType.FREE: container[FreeProxyCollector],
        ProxyType.PRIVATE: container[PrivateProxyCollector]
    }

    container[AbstractProxyCollectorService] = ProxyCollectorService

    container[AbstractProxyPoolClient] = ProxyPoolClient(container[AbstractProxyCollectorService])


def create_di_container() -> Container:
    dep_order_list: List[Callable] = [
        create_adapter_deps,
        create_proxy_pool_deps
    ]

    di_container = Container()

    for dep_setter in dep_order_list:
        dep_setter(di_container)

    return di_container
