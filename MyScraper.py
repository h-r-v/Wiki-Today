from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def get_wiki_data( date, features=['Events', 'Births', 'Deaths', 'Holidays_and_observances']):
    base = 'https://www.wikipedia.org/wiki/'
    url = base+date

    data_dict = {}

    for feature in features:
        data_dict[feature] = []
    
    try:
        r = urlopen(url)
    except HTTPError as e:
        return {'ERROR':"HTML ERROR"} #HTML Error
    except URLError as e:
        return {'ERROR':"URL ERROR"} #URLError

    bs = BeautifulSoup(r, features="html.parser")
    headings = bs.findAll('span', {'class':'mw-headline', 'id':\
                          features})

    for i,heading in enumerate(headings):
         data = heading.parent.find_next_sibling('ul').get_text()\
                .split('\n')
         #print(len(data))
         data_dict[features[i]] += data

    
    return data_dict

if __name__=='__main__':
    print(get_wiki_data( date='November_30'))
