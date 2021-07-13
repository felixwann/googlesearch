import time
from pprint import pprint
import requests
from bs4 import BeautifulSoup


class GoogleSpider:
    def __init__(self, **kwargs):
        self.keyword = kwargs.get("keyword")

    def __del__(self):
        pass

    def search(self, **kwargs) -> list:
        data = []
        if kwargs.get("keyword") is None:
            if self.keyword is None:
                return []
            else:
                query = self.keyword
        else:
            query = kwargs.get("keyword")
        query = query.replace(' ', '+')
        URL = f"http://google.com/search?q={query}"
        page = 1
        while True:
            try:
                print("当前正在搜索【" + str(query) + "】，当前第" + str(page) + "页...")
                USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
                headers = {"user-agent": USER_AGENT}
                resp = requests.get(URL, headers=headers, verify=True)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.content, "html.parser")
                    nextpage = soup.find_all("a", id="pnnext")
                    if len(nextpage) > 0 and 'href' in nextpage[0].attrs:
                        nextpage = str(nextpage[0]['href'])
                        URL = r"http://www.google.com" + nextpage
                        results = []
                        for g in soup.find_all('div', class_='g'):
                            anchors = g.find_all('a')
                            if anchors:
                                if 'href' in anchors[0].attrs:
                                    link = anchors[0]['href']
                                    title_list = list(g.find_all('h3'))
                                    if len(title_list) > 0:
                                        title_str = title_list[0]
                                        title_soup = BeautifulSoup(str(title_str), 'html.parser')
                                        title_text = title_soup.get_text()
                                        title_soup.clear()
                                        item = {
                                            "title": title_text,
                                            "link": link
                                        }
                                        results.append(item)
                        data.append({
                            page: results
                        })
                        page += 1
                        resp.close()
                        time.sleep(1)
                    else:
                        break
            except Exception as e:
                pprint(e)
                break
        return data
