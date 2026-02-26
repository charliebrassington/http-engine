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

### Proxy Pool
```python

from proxy_pool import AbstractProxyPoolClient
from bootstrap import create_di_container

container = create_di_container()

proxy_pool_client = container[AbstractProxyPoolClient]

proxy_pool_client.collect_proxies()  # CollectProxiesResponse(success=True, proxy_count=8848)

```