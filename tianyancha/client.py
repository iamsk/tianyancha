import requests


class Tianyancha(object):
    def __init__(self, token):
        self.base_url = 'http://open.api.tianyancha.com/services/open'
        self.token = token

    def get(self, path, payload):
        url = self.base_url + path
        headers = {'Authorization': self.token}
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def search(self, word):
        return self.get('/search/2.0', {'word': word})
