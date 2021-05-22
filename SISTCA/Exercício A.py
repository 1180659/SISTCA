from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()


data = cg.get_coin_market_chart_by_id(id='cardano', vs_currency='usd', days='3')
for result in data['prices']:
    print("Date,time: %s -- price: %.2f$\n" % (datetime.fromtimestamp(result[0]/1000).strftime("%m/%d/%Y, %H:%M:%S"), float(result[1])))
