# http-engine
HTTP engine to help automate web scraping including site discovery

## Roadmap features
- Proxy pool should be able to handle ratelimits, scraping free proxies (if enabled), frequency based drop-off (if dead proxy)
- Search engine simple scraper to use Bing, Yahoo, and any other search engine possible to automate for site discovery
- Html parser will involve alot of complex modular based logic for parsing different sites

## Use/Notes
This is used by me personally, so it will most likely contain only features I'd use.
This isn't an ultimate parser/scraper which will be able to automate the parsing/scraping logic of every site

## Examples

```python
from http_engine import AbstractHttpEngineClient, HttpEngineRequest, AbstractProxyPoolClient, create_di_container, DataItem

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
```
