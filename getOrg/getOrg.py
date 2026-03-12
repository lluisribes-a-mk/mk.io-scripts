import requests
import json
import jsonpath_ng as jp
from colorama import Fore, Style

token = "YOUR_TOKEN"
mkio_url = "https://api.mk.io/api/v1"

myHeaders = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + token
}

#####################
#Print token
print(f"Asking for Organization info for token: {Fore.YELLOW}{token[:6]}{Style.RESET_ALL} ...")

#####################
#Ask for Org Id

url = mkio_url + "/user/profile"
response = requests.get(url, headers=myHeaders)
response.raise_for_status()  # Launch error if not 200

json_data = response.json()
query = jp.parse('$.spec.activeOrganizationId')
matches = [match.value for match in query.find(json_data)]

active_organization_id = matches[0] if matches else None
print(f"ID of Organization: {Fore.BLUE}{active_organization_id}{Style.RESET_ALL}")

#####################
#Ask for Name
url = mkio_url + "/user/organizations/" + matches[0]
response = requests.get(url, headers=myHeaders)
response.raise_for_status()  # Launch error if not 200

json_data = response.json()
query = jp.parse('$.metadata.name')
matches = [match.value for match in query.find(json_data)]

org_name = matches[0] if matches else None
print(f"Name of Organization: {Fore.BLUE}{org_name}{Style.RESET_ALL}")
