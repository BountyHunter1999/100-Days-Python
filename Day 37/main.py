import requests
from datetime import datetime

TOKEN = "98qert456dfasg"
USERNAME = "mikeyy"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create Account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)
# print(response.text)

graph_config = {
    "id": "codegraph1",
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "float",
    "color": "sora",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create A Graph
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# View the Graph: https://pixe.la/v1/users/mikeyy/graphs/codegraph1.html

# Add Data to the Graph
data_add_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today = datetime.today()
# today = datetime(year=2022, month=1, day=18)
add_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did u code today?"),
}


response = requests.post(data_add_endpoint, json=add_params, headers=headers)
print(response.text)


# Update Data in the Graph
date_to_update = "20220118"
put_endpoint = f"{data_add_endpoint}/{date_to_update}"
put_params = {
    "quantity": "4",
}

# response = requests.put(put_endpoint, json=put_params, headers=headers)
# print(response.text)

# Delete a data pixel
date_to_delete = "20210118"
delete_endpoint = f"{data_add_endpoint}/{date_to_delete}"

# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)
