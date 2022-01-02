import requests
from plyer import notification
import json
import threading

class Interface:

    def __init__(self, url = None):
        if url == None:
            self.url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"
        else:
            self.url = url
        self.credits = "CC Alert v1.0 @DiegoDuenez 2022"
        with open('Main.json') as file:
            data = json.load(file)
            self.country = data['country']
            self.timer = data['timer']
        print(self.credits)

    def run(self):
        self.data = requests.get(self.url)
        response = self.data.json()['data']['rates'][self.country]
        #print(response)
        threading.Timer(int(self.timer), self.run).start()
        notification.notify(
        title='Bitcoin',
        message=f'${response}',
        app_icon='icon128.ico',
        app_name='CC Alert v1.0',
        )
       

            