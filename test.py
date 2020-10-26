import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 70, "name": "Ashique", "views": 20000},
        {"likes": 80, "name": "Asif", "views": 10000},
        {"likes": 90, "name": "Arif", "views": 40000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
