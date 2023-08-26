import requests
import json

def resolveIncident(sys_id):
    url = f"###{sys_id}"

    payload = json.dumps({
    "incident_state": "6"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': '###',
    'Cookie': '###'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.json()


