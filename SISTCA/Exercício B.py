from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


myportfolio = {
    "cardano": 200,
    "bitcoin": 0.003,
    "ethereum": 0.01,
    "dogecoin": 400
}

def get_prices(portfolio):
    coin_prices = {
    }

    for COIN in portfolio:
        price = cg.get_price(ids=COIN, vs_currencies="eur")
        coin_prices[COIN] = price[COIN]['eur']

    return coin_prices


def get_total_value(coin_prices,portfolio):
    valor_total = 0
    for coin in portfolio:
        value = myportfolio[coin] * coin_prices[coin]
        print("Valor em %s = %.2f€" % (coin, value))
        valor_total += value

    return valor_total


prices = get_prices(myportfolio)
total = get_total_value(prices, myportfolio)
print("Valor total do portfolio = %.2f€" % total)