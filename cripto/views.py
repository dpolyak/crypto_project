from django.shortcuts import render

def home(request):
	import requests
	import json

	# Grab crypto price date
	price_api_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,REP,DASH,IOT&tsyms=USD")
	price_api = json.loads(price_api_request.content)


	# Grab crypto news
	news_api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news_api = json.loads(news_api_request.content)

	return render(request, 'home.html', {'news': news_api, 'price': price_api})

def contact_us(request):
	return render(request, 'contacts.html', {})