import re
import requests
from bs4 import BeautifulSoup

url = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page=1&query=%eb%8d%b0%ec%9d%b4%ed%84%b0+%eb%b6%84%ec%84%9d&prefixQuery=((%3cPUBYEAR_PREFIX%3acontains%3a2020%3e))&collectionQuery=&showQuery=%eb%8d%b0%ec%9d%b4%ed%84%b0+%eb%b6%84%ec%84%9d&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue=p_2020%40%402020"
resp = requests.get(url)
resp.encoding = 'utf8'
html = resp.text


html = re.sub(r'\s{1,2}[0-9a-f]{3,4}\s{1,2}', '', html)

soup = BeautifulSoup(html, "html.parser")


for member_tag in soup.select('.result_list > li > div.list_con > p.title > a'):
    name = member_tag.text
    link = member_tag['href']

    matched = re.search(r'\d+', link)
    if matched:
        member_id = matched.group(0)
    else:
        member_id = None

    print(name, member_id)
