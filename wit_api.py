import os
from wit import Wit

class WitApi:
    def retrieve_token():
        return os.environ["WIT_TOKEN"]

    def __init__(self):
        self.token =  WitApi.retrieve_token()
        self.wit_client = Wit(self.token)

    def send_text(self, text):
        return self.wit_client.message(text)
