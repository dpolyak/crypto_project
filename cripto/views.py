from django.shortcuts import render

def home(request):
	import requests
	import json

	# Grab crypto multi price date
	price_multi_api_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,REP,DASH,IOT&tsyms=USD")
	price_multi_api = json.loads(price_multi_api_request.content)


	# Grab crypto news
	news_api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news_api = json.loads(news_api_request.content)

	return render(request, 'home.html', {'news': news_api, 'price': price_multi_api})
