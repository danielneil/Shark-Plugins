import requests

url = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1597883791&period2=1629419791&interval=1d&events=history&includeAdjustedClose=true'

r = requests.get(url, allow_redirects=True)

open('facebook.ico', 'wb').write(r.content)
