import requests
from bs4 import BeautifulSoup

#raw = requests.get("https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=38&start="+str(n)+"&refresh_start=0")
                    #https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=18&start=11&refresh_start=0
#html = BeautifulSoup(raw.text, "html.parser") #해당 url에 담긴 html페이지를 가져와서 저장함

#container = html.select("ul.type01 > li")

#title = container[0].select_one("a._sp_each_title") #클래스 선택자는 . 아이디 선택자는 #으로 가져온다
#태그 안 텍스트 데이터만 가져오기 위해서는 아래와 같이 text함수를 사용해야 한다.
#title = container[0].select_one("a._sp_each_title").text

f = open("naver_news.csv","w")
f.write("언론사, 뉴스제목\n") #분류

for n in range(1, 21, 10):

    raw = requests.get("https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=38&start="+str(n)+"&refresh_start=0")

    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("ul.type01 > li")

    for i in range(0,10):
        title = container[i].select_one("a._sp_each_title").text
        media = container[i].select_one("span._sp_each_source").text

        #print(title)

        title = title.replace(",", "")
        media = media[:-6] # 불필요하게 들어간 부분은 문자열 슬라이싱을 통해서 제거해 줄 수 있다.
        f.write(media + "," + title + "\n")

f.close()#파일을 열면 꼭 닫아주어야 한다.