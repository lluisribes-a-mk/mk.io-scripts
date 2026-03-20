
"""
MK.IO Interactive Asset Cleanup Tool
------------------------------------
This script provides a very basic controlled interface to manage and selectively delete 
all media assets from a user's project using the MK.IO Media API.

Functional Workflow:
1. Retrieval: Executes an HTTP GET request to list all assets within the 
   'project_name' project.
2. Filtering: Locally identifies assets created by 'target_user' by analyzing the 'createdBy' 
   field in the 'systemData' metadata object.
3. Interactive Confirmation: Iterates through matching assets, presenting 
   each asset name to the user for manual confirmation.
4. Execution: Upon a 'yes' response, it triggers an HTTP DELETE request to 
   permanently remove the asset record from the MK.IO platform.

Objective:
To enable supervised maintenance of project resources, ensuring that only 
specifically confirmed assets are removed, thereby preventing accidental 
data loss.
"""


import requests

# Initial configuration
# Your personal API token from MK.IO settings
token = "YOUR_TOKEN_HERE"
# Base URL for the MK.IO Media API
mkio_url = "https://api.mk.io/api/v1"
project_name = "YOUR_PROJECT_NAME_HERE"
target_user = "YOUR_TARGET_USER_HERE"

# API headers with Bearer token authentication
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {token}"
}

# 1. Retrieve the full list of assets from the project
list_url = f"{mkio_url}/projects/{project_name}/media/assets"
response = requests.get(list_url, headers=headers)

if response.status_code == 200:
    # The API returns a list of assets in the 'value' field
    assets = response.json().get('value', [])
    
    # 2. Filter assets where systemData.createdBy matches our target user
    filtered_assets = [
        asset for asset in assets 
        if asset.get('systemData', {}).get('createdBy') == target_user
    ]
    
    print(f"Found {len(filtered_assets)} assets created by {target_user}.\n")

    # 3. Interactive loop for selective deletion
    for asset in filtered_assets:
        asset_name = asset['name']
        asset_id = asset['id']
        
        # Ask the user for confirmation
        choice = input(f"Do you want to delete asset '{asset_name}'? (yes/no): ").strip().lower()
        
        if choice in ['yes', 'y']:
            # Construct the specific endpoint for the asset deletion
            delete_url = f"{mkio_url}/projects/{project_name}/media/assets/{asset_name}"
            
            # Execute the HTTP DELETE request
            delete_res = requests.delete(delete_url, headers=headers)
            
            # 200 means deleted, 204 means it didn't exist but the result is the same
            if delete_res.status_code in [3, 4]:
                print(f"  Successfully deleted asset: {asset_name}\n")
            else:
                print(f"  Failed to delete asset {asset_name}: {delete_res.status_code}")
                # Print error details if the API provides them
                print(delete_res.text + "\n")
        else:
            print(f"  Skipping asset: {asset_name}\n")
            
    print("Process completed.")
else:
    print(f"Error retrieving assets: {response.status_code}")
    print(response.text)