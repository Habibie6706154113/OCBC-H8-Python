from app import connex_app
import unittest

class MyTestCase(unittest.TestCase):

    def test_get_all_director(self):
        connex_app.app.testing = True
        result = connex_app.app.test_client().get('/api/directors')
        # Make your assertions
        self.assertEqual(result.status_code, 200)

    def test_get_all_movie(self):
        connex_app.app.testing = True
        result = connex_app.app.test_client().get('/api/movies')
        # Make your assertions
        self.assertEqual(result.status_code, 200)

    def test_get_five_best_movie(self):
        connex_app.app.testing = True
        result = connex_app.app.test_client().get('/api/five_best_movies')
        # Make your assertions
        self.assertEqual(result.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()