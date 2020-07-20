from bs4 import BeautifulSoup
import requests


print("""

███████╗ ██████╗ ██╗     ██╗
██╔════╝██╔═══██╗██║     ██║
███████╗██║   ██║██║     ██║
╚════██║██║▄▄ ██║██║     ██║
███████║╚██████╔╝███████╗██║
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝
                            
""")
headers = {'apikey': 'YOUR API KEY'}
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/47.0.2526.106 Safari/537.36'}
dork = str(input('Google Dork: '))
params = (
    ("q", dork),
    ("device", "desktop"),
    ("num", "100")
)

# To save links to a text file
# sys.stdout = open("output.txt", "w")

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params).json()

for i in response['organic']:
    url = i['url'] + "'"
    try:
        res = requests.get(url, headers=user_agent)
    except:
        continue
    soup = BeautifulSoup(res.text, 'html.parser')
    if 'sql' in soup.text:
        print(f'{url} is sql vulnerable')
    elif 'SQL' in soup.text:
        print(f'{url} is sql vulnerable')
    else:
        continue

# sys.stdout.close()