import requests
import json
from fakeDictionary import fakeDictionary

def createIncident(uri, alertID, description):
    url = "###"

    payload = json.dumps({
      "assignment_group": "CSS",
      "u_external_reference": alertID,
      "short_description": "HPE OneView1 Alert: " + alertID,
      "urgency": "2",
      "impact": "2",
      "comments": description + " Link to an alert: " + uri, 
      "category": "failure"
    })

    headers = {
      'Content-Type': 'application/json',
      'Authorization': '###',
      'Cookie': '###'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return (response.json())
