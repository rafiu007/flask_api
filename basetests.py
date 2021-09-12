import unittest
import json

from app import app
#from database.db import db

app.testing = True


class baseTest(unittest.TestCase):
    # check response
    def apiTest(self):
        tester = app.test_client(self)
        response = tester.get('/greet', headers={"Content-Type": "application/json"})
        self.assertEqual(2000, response.status_code)

    def checkType(self):
        tester = app.test_client(self)
        response = tester.get('/greet', headers={"Content-Type": "application/json"})
        self.assertEqual(str, response.content_type)

if __name__ == "__main__":
    unittest.main()