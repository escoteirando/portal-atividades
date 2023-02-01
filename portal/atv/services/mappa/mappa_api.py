import json

import urllib3

from .mappa_models import MappaLoginResponse, MappaDadosEscotista

MAPPA_PROXY = 'https://mappa-proxy.fly.dev/'


class MappaApi:
    http = urllib3.PoolManager()

    def __init__(self, base_url: str = 'https://mappa-proxy.fly.dev'):
        self.base_url = base_url.removesuffix('/')

    def login(self, username: str, password: str) -> MappaLoginResponse:
        url = f'{self.base_url}/mappa/login'
        body = json.dumps(
            dict(username=username, password=password)).encode('utf-8')
        r = self.http.request('POST', url,
                              body=body,
                              headers={'Content-Type': 'application/json'})
        body = json.loads(r.data.decode('utf-8'))
        return MappaLoginResponse(body)

    def get_escotista(self, user_id: int, authorization: str) -> MappaDadosEscotista:
        url = f'{self.base_url}/mappa/escotista/{user_id}'
        r = self.http.request('GET', url, headers={
                              'Authorization': authorization})
        body = json.loads(r.data.decode('utf-8'))
        return MappaDadosEscotista(body)
