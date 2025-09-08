import requests
from bs4 import BeautifulSoup as bs
from config import clauses

with requests.Session() as s:
    r = s.get("https://chartink.com/screener")
    soup = bs(r.content, 'html.parser')
    s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']

    for filename in clauses:
        f = open(f"./Output/{filename}.txt", "w")
        nsecodes = []
        for clause in clauses[filename]:
            body = { 'scan_clause': clause}
            response = s.post('https://chartink.com/screener/process', data=body).json()
            nsecodes.extend(list(map(lambda x: x["nsecode"], response["data"])))
            
        for code in set(nsecodes):
            name = code.replace("&", "_") # Added for TradingView Support
            name = name.replace("-", "_") # Added for TradingView Support
            f.write(f'NSE:{name}, \n')

    f.close()
