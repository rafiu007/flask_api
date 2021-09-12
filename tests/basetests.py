import unittest
import json

from app import app
#from database.db import db


class baseTest(unittest.TestCase):
    # check response
    def apiTest(self):
        tester = app.test_client(self)
        response = tester.get('/greet', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()