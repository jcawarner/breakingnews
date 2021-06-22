from django.shortcuts import render
import requests
import json



def general(request):
	url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&categories=general"

	response = requests.get(url)
	generalnews = json.loads(response.content)

	return render(request, 'general.html', {'generalnews': generalnews})

def science(request):
	url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&categories=science"

	response = requests.get(url)
	sciencenews = json.loads(response.content)

	return render(request, 'science.html', {'sciencenews': sciencenews})

def technology(request):
	url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&categories=technology"

	response = requests.get(url)
	technews = json.loads(response.content)

	return render(request, 'technology.html', {'technews': technews})


def business(request):
	url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&categories=business"

	response = requests.get(url)
	businews = json.loads(response.content)

	return render(request, 'business.html', {'businews': businews})

def health(request):
	url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&categories=health"

	response = requests.get(url)
	healthnews = json.loads(response.content)

	return render(request, 'health.html', {'healthnews': healthnews})

def entertainment(request):
	url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&categories=entertainment"

	response = requests.get(url)
	entertain = json.loads(response.content)

	return render(request, 'entertainment.html', {'entertain': entertain})



def social(request):
	url = "https://socialanimal.p.rapidapi.com/api/v1/search"

	payload = """{
    \"query\": {
        \"title\": \"digital marketing\"
    }
}"""


	headers = {
	    'content-type': "application/json",
	    'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8",
	    'x-rapidapi-host': "socialanimal.p.rapidapi.com"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)
	social = json.loads(response.content)

	return render(request, 'social.html', {'social':social})

def search(request):
	if request.method == 'POST':
		keywords = request.POST['keyword']
		url = "http://api.mediastack.com/v1/news?access_key=c6becc1dd8bf7b8dbfe9a21d98911653&languages=en&keywords=" + str(keywords)
		response = requests.get(url)
		keysearch = json.loads(response.content)
		return render(request, 'search.html', {'keysearch':keysearch})

	else:
		return render(request, 'search.html', {})

