import requests
import json
import config

class NewsAPI:

  def __init__(self):
    self.api_key = config.API_KEY
    self.api_secret = config.API_SECRET
    self.url = config.URL

  def get_news(self):

    headers = {
      "accept": "application/json",
      "APCA-API-KEY-ID": self.api_key, 
      "APCA-API-SECRET-KEY": self.api_secret
    }

    response = requests.get(self.url, headers=headers)
    news_data = response.json()

    return news_data

if __name__ == '__main__':

  api = NewsAPI()
  news = api.get_news()

  print(json.dumps(news, indent=4))
