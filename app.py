import sys
import requests
import bs4
import webbrowser
import pprint
import pyperclip as clipboard

print('Searching...')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
url = 'https://www.google.com/search?q='

if len(sys.argv) > 1:
    keyword = ' '.join(sys.argv[1:])
else:
    keyword = clipboard.paste()

query = url + keyword
res = requests.get(query, headers= headers)

parsed = bs4.BeautifulSoup(res.text, 'html.parser')
g_link = parsed.select('.r a')
links_filtered = [link.get('href') for link in g_link if '#' not in str(link) if 'webcache' not in str(link)]

for link in links_filtered:
    webbrowser.open_new_tab(link)