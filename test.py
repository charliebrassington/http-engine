from proxy_pool import AbstractProxyPoolClient
from bootstrap import create_di_container

container = create_di_container()

proxy_pool_client = container[AbstractProxyPoolClient]

response = proxy_pool_client.collect_proxies()

print(response)
