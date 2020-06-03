# billBoardDevOps

A Python Flask web Restfull API to scrape data off [Billboard.com](https://www.billboard.com/charts/hot-100), for fetching the weekly Top100 using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) package

Create container using:
```python
docker build -f Dockerfile -t <dockerhub/repo> .
docker push <dockerhub/repo>

