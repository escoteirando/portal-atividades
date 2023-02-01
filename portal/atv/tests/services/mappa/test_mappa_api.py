import unittest
from datetime import datetime

from atv.services.mappa.mappa_api import MappaApi


class TestMappaApi(unittest.TestCase):

    def test_login(self):
        api = MappaApi('https://mappa-proxy.fly.dev')
        login_response = api.login(username='guionardo', password='A1GU')
        self.assertTrue(login_response.valid_until > datetime.now())

        escotista = api.get_escotista(
            login_response.user_id, login_response.auth)
        self.assertEqual('Guionardo', escotista.escotista.username)
