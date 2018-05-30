# encoding=utf-8
#
#云月港爬虫
#
import re
import codecs
#codecs: 自然语言编码转换模块
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://www.danji360.com/forum-74-1.html'

def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

#伪造浏览器请求头，获取页面代码

def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    game_list=soup.find('table',attrs={'id': 'threadlisttableid'})
    game_name_list=[]
    # print game_list
    
    
    game_tobady = game_list.find_all('tr')
    print len(game_tobady)
    # print game_tobady[0]
    num=0
    for num in range(len(game_tobady)):
            detail =  game_tobady[num].find('th',attrs={'class':{'common','new'}})
            #查找class名为common和new的th标签
            # print detail
            if detail:
                # game_url=detail.find('a',href=re.compile('html'))
                game_detail = detail.find('a',href=re.compile('html'))
                game_name=game_detail.getText()
                print game_name
                game_name_list.append(game_name)
                # print(game_url['href'])
    
    return game_name_list
  

def main():
    with codecs.open('games', 'wb', encoding='utf-8') as fp:
         url = DOWNLOAD_URL
         html = download_page(url)
         games=parse_html(html)
        #  print games
         fp.write(u'{games}\n'.format(games='\n'.join(games)))
      

if __name__ == '__main__':
    main()
