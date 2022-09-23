import requests
from datetime import datetime

USERNAME= "krush25"
TOKEN = "hodnfnfjgbttuhgb"
ID = "graph1"
pixela_end_point = "https://pixe.la/v1/users"
pixela_parameters= {
    "token":USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_end_point , json=pixela_parameters)
# print(response.text)

graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"
graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_end_point,json=graph_config,headers=headers)
# print(response.text)

add_pixel_end_point= f"{graph_end_point}/{ID}"

today = datetime(year=2022,month=1,day=16)
DATE = today.strftime("%Y%m%d")
add_pixel_config = {
    "date": DATE,
    "quantity": "18"
}
add_pixel_header = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=add_pixel_end_point, json= add_pixel_config,headers=add_pixel_header)
# print(response.text)

update_pixel_endpoint = f"{add_pixel_end_point}/{DATE}"
update_pixel_config = {
    "quantity": "8"
}
# response = requests.put(url=update_pixel_endpoint,json=update_pixel_config,headers=headers)
# print(response.text)

delete_response = requests.delete(url=update_pixel_endpoint,headers=headers)
print(delete_response)