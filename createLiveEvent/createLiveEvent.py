import requests

token = "YOUR_TOKEN"
mkio_url = "https://api.mk.io/api/v1/projects/"
project_name = "YOUR_PROJECT_NAME"
name_live = "live-event-1"
storage_repo = "YOUR_STORAGE_REPO"


#####################
#Create
url = mkio_url + project_name + "/media/liveEvents/"+name_live

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + token
}

payload = { "properties": {
        "encoding": {
            "encodingType": "Premium1080p",
            "keyFrameInterval": "PT2S"
        },
        "input": {
            "streamingProtocol": "SRT",
            "timedMetadataEndpoints": [{ "url": "bce" }],
            "keyFrameIntervalDuration": "2"
        },
        "preview": { "streamingPolicyName": "Predefined_ClearStreamingOnly" },
        "streamOptions": ["Default"],
        "useStaticHostname": True
    } }

response = requests.put(url, json=payload, headers=headers)

print("Creating the Live Event: " + name_live)
print(response.text)

#####################
#Create DVR Asset
url = mkio_url + project_name + "/media/assets/assetDVR-" + name_live

payload = { "properties": {
        "storageAccountName": storage_repo,
        "containerDeletionPolicy": "Delete",
        "description": "Asset Generated from a LiveEvent",
        "storageEncryptionFormat": "None"
    } }

response = requests.put(url, json=payload, headers=headers)

#print(response.text)
print("Creating the DVR asset: assetDVR-" + name_live)
print(response)

#####################
#Associate DVR Asset to Live
url = mkio_url + project_name + "/media/liveEvents/"+ name_live + "/liveOutputs/assetDVR-" + name_live


payload = { "properties": {
        "hls": { "fragmentsPerTsSegment": 1 },
        "outputSnapTime": 0,
        "archiveWindowLength": "PT30M",
        "assetName": "assetDVR-" + name_live
    } }

response = requests.put(url, json=payload, headers=headers)

#print(response.text)
print("Associating the DVR asset to the Live Event")
print(response)

####################
#Create a Locator
url = mkio_url + project_name + "/media/streamingLocators/"+ name_live + "-locator"


payload = { "properties": {
        "suppressed": False,
        "assetName": "assetDVR-" + name_live,
        "streamingPolicyName": "Predefined_DownloadAndClearStreaming"
    } }

response = requests.put(url, json=payload, headers=headers)

#print(response.text)
print("Creating the locator: " + name_live + "-locator")
print(response)