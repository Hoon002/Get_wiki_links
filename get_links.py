import wikipediaapi
import requests
import time
import os

class WikiManage:
    
    def __init__(self):
        pass

    def random_pages(self):
        S = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "500"
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        RANDOMS = DATA["query"]["random"]

        wiki_pages = []
        for r in RANDOMS:
            if r["ns"] != 0:
                continue
            wiki_pages.append(r["title"])
        
        return wiki_pages


    def get_links(self, page):

        links = page.links

        filename = str(page).replace(':', '=')

        with open('./'+ foldername + '/' + filename + '.txt', 'w', encoding='utf-8') as f:

            for title in sorted(links.keys()):
                f.write("%s\n" %links[title])

if __name__ == "__main__":
    wiki_wiki = wikipediaapi.Wikipedia('en')

    print('무작위로 위키백과 페이지를 추출합니다.\n오류가 발생하면 프로그램을 다시 실행하십시오.\n제작: 임영훈\n')
    pages_to_search = WikiManage().random_pages() #랜덤 페이지 제목들 모으기 list

    print('새로운 폴더를 생성합니다.\n')
    foldername = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(time.time())) # 폴더 명 = 생성 날짜시간
    path = './'+foldername
    os.mkdir(path)

    print('페이지의 하이퍼링크들을 불러옵니다.\n완료되면 자동으로 종료됩니다.')
    for each_page in pages_to_search:
        page_py = wiki_wiki.page(each_page)
        WikiManage().get_links(page_py)