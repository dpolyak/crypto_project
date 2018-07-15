from django.shortcuts import render

def home(request):
	import requests
	import json

	# Grab crypto full price data
	price_full_api_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,REP,DASH,IOT&tsyms=USD")
	price_full_api = json.loads(price_full_api_request.content)


	# Grab crypto news
	news_api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news_api = json.loads(news_api_request.content)

	return render(request, 'home.html', {'news': news_api, 'price_full': price_full_api})
