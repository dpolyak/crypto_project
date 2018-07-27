from django.shortcuts import render
import requests
import json

def home(request):
	# Grab crypto full price data
	price_full_api_request = requests.get(
		"https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,TRX,REP,DASH&tsyms=USD")
	price_full_api = json.loads(price_full_api_request.content)


	# Grab crypto news
	news_api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news_api = json.loads(news_api_request.content)

	return render(request, 'home.html', {'news': news_api, 'price_full': price_full_api})


def prices(request):

	if request.method == 'POST':
		quote = request.POST['quote']
		quote = quote.upper()
		quote_full_api_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=%s&tsyms=USD" % quote)
		price_full_api = json.loads(quote_full_api_request.content)

		return render(request, 'prices.html', {'quote':quote, 'price_data':price_full_api})
	else:
		notfound = "Enter a crypto currency symbol into the form above ..."
		return render(request, 'prices.html', {"notfound": notfound})
