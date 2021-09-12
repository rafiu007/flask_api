import json

from tests.basetests import baseTest

class apiTest(baseTest):

    def testapi(self):
            response = self.app.get('/greet', headers={"Content-Type": "application/json"})
            self.assertEqual(1, response.status_code)
