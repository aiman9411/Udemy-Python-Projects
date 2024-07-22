import requests

connection = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data = connection.json()
question_data = data["results"]