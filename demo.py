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
    curTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file = "./results/googlesearch" + keyword + "_" + curTime + ".json"
    with open(file, "w", encoding="utf-8") as f:
        f.write(str(j))
