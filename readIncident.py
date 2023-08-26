import requests

def readIncident():
  url = "###"

  payload = {}
  headers = {
    'Authorization': '###',
    'Cookie': '###'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  try:
    return response.json()["result"]
  except:
    temp=[]
    return temp

