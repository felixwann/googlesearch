import json
import time
from datetime import datetime
from pprint import pprint

from GoogleSpider import GoogleSpider

if __name__ == "__main__":
    gs = GoogleSpider()
    keyword = "china"
    data = gs.search(keyword=keyword)
    j = json.dumps(data)
    pprint(j)
