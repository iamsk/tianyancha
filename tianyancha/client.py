import os
import requests
import json
import pathlib


class Tianyancha(object):
    def __init__(self, token):
        self.base_url = 'http://open.api.tianyancha.com/services/open/'
        self.token = token
        self.api_mappings = self.gen_api_mappings()
        self.methods = [k for k in self.api_mappings.keys()]
        self.gen_methods()

    def get(self, path, payload):
        url = self.base_url + path
        headers = {'Authorization': self.token}
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def search(self, word):
        # replaced with generated method, but works the same
        return self.get('search/2.0', {'word': word})

    @classmethod
    def gen_api_mappings(cls):
        # from https://open.tianyancha.com/api_tool
        file_name = os.path.join(pathlib.Path(__file__).parent.absolute(), 'apilist.json')
        f = open(file_name)
        data = json.load(f)
        mappings = {}
        for sub in data:
            items = sub['children']
            for item in items:
                name = item['data']['fname']
                desc = item['data']['fdesc']
                path = item['data']['openUrl'].replace('/services/open/', '')
                method = path.replace('/2.0', '').replace('/', '_')
                params = json.loads(item['data']['requestParam']).keys()
                mappings[method] = {'name': name, 'desc': desc, 'path': path, 'params': [k for k in params]}
        return mappings

    def gen_methods(self):
        for k, v in self.api_mappings.items():
            self.add_method(k, v)

    def add_method(self, k, v):
        def inner(**payload):
            return self.get(v['path'], payload)

        inner.__name__ = k
        inner.__doc__ = v['name']
        inner.__desc__ = v['desc']
        inner.__params__ = v['params']
        setattr(self, inner.__name__, inner)


if __name__ == '__main__':
    t = Tianyancha('')
    for k, v in t.api_mappings.items():
        print('#### {}'.format(v['name']))
        print('\n')
        print('*', 'method: ', k)
        for kk, vv in v.items():
            print('*', kk, vv)
        print('\n')
    # print(t.search(word='气味图书馆'))
    # print(len(t.methods))
    # print(t.methods)
    # print(json.dumps(t.api_mappings, indent=4, sort_keys=True))
