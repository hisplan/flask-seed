import os
import unittest
import tempfile
import my_web


class MyWebTestCase(unittest.TestCase):

    def setUp(self):        
        self.app = my_web.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        resp = self.app.get('/')
        assert resp.status_code == 200
        assert '<h1>Hello, World!</h1>' == resp.data

    def test_page_not_found(self):
        resp = self.app.get('/asdfarge')
        assert resp.status_code == 404, 'Must return HTTP status code 404'

    def test_show_user_profile(self):
        resp = self.app.get('/user/Jaeyoung')
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
