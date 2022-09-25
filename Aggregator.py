import requests
from bs4 import BeautifulSoup as bs
from config import clauses

with requests.Session() as s:
    r = s.get('https://chartink.com/')
    soup = bs(r.content, 'lxml')
    s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']

    f = open("./Output/IB_Output.txt", "w")
    for clause in clauses:
        body = { 'scan_clause': clause}
        response = s.post('https://chartink.com/screener/process', data=body).json()
        nsecodes = list(map(lambda x: x["nsecode"], response["data"]))
        for name in nsecodes:
            f.write(f'{name}, \n')

    f.close()