import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd

def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()

xhtml = url_get_contents('https://pokemondb.net/pokedex/all').decode('utf-8')

p = HTMLTableParser()
p.feed(xhtml)
pprint(p.tables[0])

print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[0]))

pd.DataFrame(p.tables[0]).to_csv('S:\local.store\dev\py\scraping\pokemon\pokemon_db.csv')
