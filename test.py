from http_engine import AbstractHttpEngineClient, HttpEngineRequest
from proxy_pool import AbstractProxyPoolClient
from bootstrap import create_di_container
from domain.models import DataItem

container = create_di_container()

http_engine = container[AbstractHttpEngineClient]
proxy_pool = container[AbstractProxyPoolClient]

proxy_pool.collect_proxies()

response = http_engine.send_http_request(http_request=HttpEngineRequest(
    method="get",
    url="https://medal.tv/u/Alfxz",
    wanted_data_items=[
        DataItem(name="discord_id", keywords=["discord", "id"])
    ],
    proxy_pool_enabled=True
))

print(response)
