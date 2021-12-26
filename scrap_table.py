import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd

def url_get_contents(url):
    req = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/95.0.2'})
    f = urllib.request.urlopen(req)
    return f.read()

xhtml = url_get_contents('https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number').decode('utf-8')

p = HTMLTableParser()
p.feed(xhtml)
pprint(p.tables[8])

print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[8]))

pd.DataFrame(p.tables[8]).to_csv('S:\local.store\dev\py\scraping\pokemon\pokemon_db_VIII.csv')