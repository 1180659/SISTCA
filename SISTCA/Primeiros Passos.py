from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# Executar primeiro, isolado e depois eliminar
############################################
coin_list = cg.get_coins_list()
print(coin_list)
############################################


def get_coin_price():
    coin_id = input("Escreva o id da cripto moeda: ")
    par = input("Introduza o par de comparação: ")
    price = cg.get_price(ids=coin_id, vs_currencies=par)
    print(price)


get_coin_price()
