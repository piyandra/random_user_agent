import requests

class Random:
    def __init__(self):
        self._apikey = "glbbLNMBxjNgMAV8IbL3Tvf163oARD4T"

    def get_apikey(self):
        return self._apikey

    def set_apikey(self, apikey):
        self._apikey = apikey

    def randomua(self):
        header = {"apikey" : self.get_apikey()}
        payload = {}
        endpoint = "https://api.apilayer.com/user_agent/generate?mobile=true&android=true"
        return requests.get(endpoint, headers=header, data=payload).json()['ua']



