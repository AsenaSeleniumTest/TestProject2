import requests
import json

class TestAPI():
    BASE_URL="http://216.10.245.166"
    ADD_BOOK_POST = "/Library/Addbook.php"
    JSON_POST = {
    "name":"The Python bible",
    "isbn":"1000000001",
    "aisle":"1000020",
    "author":"LORDUSBQ"
     }
    
    def post_request(self):
        json_data = json.dumps(self.JSON_POST)
        response = requests.post(f"{self.BASE_URL}{self.ADD_BOOK_POST}",json_data,timeout=2500)
        data = response.json()
        print(data.text())
api_test = TestAPI

api_test.post_request
        