
"""
MK.IO Asset Policy Updater
--------------------------
This script utilizes the MK.IO Media API to manage and perform bulk updates on the 
deletion policies of media assets within a project

Functional Logic:
1. Retrieval: It performs an HTTP GET request to the Assets endpoint to retrieve a 
   comprehensive list of all assets associated with the project
2. Filtering: The script processes the response locally, inspecting the 'systemData' 
   metadata object to filter for assets created by a specific user identity 
   (defined by the 'createdBy' field). The variable 'target_user' holds the value of
   the user identity to match against
3. Transformation: For each matching asset, it executes an HTTP PUT request to the 
   specific asset resource URL to update its properties
4. Policy Update: It sets the 'containerDeletionPolicy' to "Delete". Per the API 
   specification, this requires including the mandatory 'storageAccountName' in the 
   request body

Objective:
The primary goal is to ensure that when an asset is eventually deleted from 
the MK.IO platform in the future, the linked remote storage container and 
all its contents are automatically removed rather than being retained by default.
This automation helps in managing cloud storage lifecycles and avoiding redundant 
storage costs.
"""

import requests
import json

token = "YOUR_TOKEN_HERE"
mkio_url = "https://api.mk.io/api/v1"
project_name = "YOUR_PROJECT_NAME_HERE"
target_user = "YOUR_TARGET_USER_HERE"

myHeaders = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + token
}


url = mkio_url + "/projects/" + project_name + "/media/assets"

response = requests.get(url, headers=myHeaders)

if response.status_code == 200:
    # The API response contains a list of assets in the 'value' field
    data = response.json()
    assets = data.get('value', [])
    
    # Filter the assets where systemData.createdBy matches the target user
    filtered_assets = [
        asset 
        for asset in assets 
        if asset.get('systemData', {}).get('createdBy') == target_user
    ]
      # Display the list of found IDs
    print(f"Found {len(filtered_assets)} assets created by {target_user}. Updating policies...")  

for asset in filtered_assets:
        asset_name = asset['name']
        # The storageAccountName is required for the update payload
        storage_account = asset['properties']['storageAccountName']
        
        # Endpoint for updating a specific asset [1, 8]
        update_url = f"{mkio_url}/projects/{project_name}/media/assets/{asset_name}"
        
        # Prepare the payload to change the deletion policy to 'Delete' [4, 5]
        update_data = {
            "properties": {
                "storageAccountName": storage_account,
                "containerDeletionPolicy": "Delete"
            }
        }
        
        # Execute the HTTP PUT request to update the asset [2]
        update_res = requests.put(update_url, headers=myHeaders, json=update_data)
        
        if update_res.status_code == 200:
            print(f"Successfully updated asset: {asset_name}")
        else:
            print(f"Failed to update asset {asset_name}: {update_res.status_code}")
            print(update_res.text)
else:
    print(f"Error listing assets: {response.status_code}")