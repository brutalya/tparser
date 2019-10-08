import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
base_url = 'http://rutor.info/search/spider%20man'

def hh_parse(base_url,headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content,'html.parser')
        divs = soup.find_all('tr', attrs = {'class':'gai','class':'tum'})
        for div in divs:
            tds=div.find_all('td')
            print(tds[0].text)
            aa=tds[1].find_all('a')
            print(aa[0]['href'])
            print(aa[1]['href'])
            print(aa[2]['href'])
            print(aa[2].text)
            print(tds[2].text)
            green=tds[3].find('span', attrs={'class':'green'})
            print(green)
            red = tds[3].find('span', attrs={'class': 'red'})
            print(red)
            #magnet_href=aa[0]['href']
            #title = div.find('div', attrs = {'class':'resume-search-item__name'}).text
            #href = div.find('a',attrs={'class':'downgif'})['href']
            #company = div.find('a',attrs={'data-qa':'vacancy-serp__vacancy-employer'}).text
            #print(title+' --- '+href+' -- '+company)
            print(len(tds))
        print(len(divs))
        print('Ok')
    else:
        print('ERROR')


hh_parse(base_url,headers)