from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def get_wiki_data( date, features=['Events', 'Births', 'Deaths', 'Holidays_and_observances']):
    base = 'https://www.wikipedia.org/wiki/'
    url = base+date

    try:
        r = urlopen(url)
    except HTTPError as e:
        return -1 #HTML Error
    except URLError as e:
        return -2 #URLError

    bs = BeautifulSoup(r)
    headings = bs.findAll('span', {'class':'mw-headline', 'id':\
                          features})

    for heading in headings:
        print( heading.parent.find_next_sibling('ul').get_text(), \
            end='\n\n')
