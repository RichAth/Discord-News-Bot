# Need: python 3.x
# Need: Rapid-API Key for google news - https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/google-news 
# Need: To install dependancies run: pip install -r requirements.txt

import requests
import random
from discord import Webhook, RequestsWebhookAdapter

# Rapid API for Google news
url = "https://google-news.p.rapidapi.com/v1/source_search"

# For news topics and options visit:
# https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/google-news
querystring = {"source":"techcrunch.com","lang":"en", "when":"1d"} #,"country":"AU"

# Need to get API-key
headers = {
	"X-RapidAPI-Key": "Insert API Key HERE",
	"X-RapidAPI-Host": "google-news.p.rapidapi.com"
}

# Discord Channel Web Hook - created in channel settings: https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks#what-do-webhooks-do-in-discord
webhook = Webhook.from_url("Insert Webhook URl HERE", adapter=RequestsWebhookAdapter())

try:
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    
    #Pick 3 random articles
    for i in range(3):
        articleNum = random.randint(0, len(jsonResponse["articles"])) 
        title = jsonResponse["articles"][articleNum]["title"]
        link = jsonResponse["articles"][articleNum]["link"]  
        # Post to discord channel
        webhook.send(title)
        webhook.send(link)

#Catch Http Errors 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
