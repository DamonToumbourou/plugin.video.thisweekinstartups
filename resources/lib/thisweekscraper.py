from bs4 import BeautifulSoup as bs
import requests
import re


def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    return soup


def get_latest(url, keyword):
    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'feed-item-dismissable '})
    output = []

    for i in content:
        section = i.find('span', {'class': 'branded-page-module-title-text'}).get_text()
        if keyword in section:
            link = i.find_all('div', {'class': 'yt-lockup-dismissable'})
            
            for k in link:
                label_path = k.find('h3', {'class': 'yt-lockup-title '}).find('a')
                label = label_path.get('title')
                print 'label: '
                print label
            
                path = label_path.get('href')
                path = re.search(r'\=(.*)', path).group(0)
                print 'path: '
                print path
                
                img = k.find('img')['data-thumb']
                img = 'http:' + img 
                print 'img: '
                print img

                item = {
                    'label': label,
                    'path': path,
                    'thumbnail': img,
                }

                output.append(item)

    return output
get_latest('https://www.youtube.com/user/ThisWeekIn', 'Uploads')
