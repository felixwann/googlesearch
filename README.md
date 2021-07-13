### 安装依赖
```
pip install requests
pip install beautifulsoup4
```
```python
from GoogleSpider import GoogleSpider

if __name__ == "__main__":
    gs = GoogleSpider()
    keyword = "china"
    data = gs.search(keyword=keyword)
    print(data)

```
