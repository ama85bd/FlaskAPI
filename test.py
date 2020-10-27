import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 70, "name": "Ashique", "views": 20000},
#         {"likes": 80, "name": "Asif", "views": 10000},
#         {"likes": 90, "name": "Arif", "views": 40000}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())
#
# input()
# response = requests.get(BASE + "video/12")
# print(response.json())


# response = requests.patch(BASE + "video/2", {'views':1000})
# print(response.json())

response = requests.delete(BASE + "video/2")
print(response)