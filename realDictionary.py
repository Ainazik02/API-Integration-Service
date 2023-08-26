import requests
import json
import urllib3

def realDictionary():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def returnToken(oneViewInstance):
        url = f"https://{oneViewInstance}/rest/login-sessions"
        payload = json.dumps({
        "authLoginDomain": "",
        "password": "###",
        "userName": "###"
        })
        headers = {
        'Content-Type': 'application/json'
        }
        APItoken = requests.request("POST", url, headers=headers, data = payload, verify=False)
        return APItoken.json()["sessionID"]

    def oneViewStateFunc(oneViewInstance, oneViewState, APItoken):
        url = f"https://{oneViewInstance}/rest/alerts?filter=\"severity EQ 'Critical'\"&filter=\"alertState EQ '{oneViewState}'\""
        headers = {
        'Auth': APItoken
        }
        payload ={}
        response = requests.request("GET", url, headers=headers, data = payload, verify=False)
        return response.json()

    oneViewList = [ 
            { 
                "name": "###", 
                "state": "Locked" 
            }, 
            { 
                "name": "###", 
                "state": "Active" 
            }, 
            { 
                "name": "###", 
                "state": "Locked" 
            }, 
            { 
                "name": "###", 
                "state": "Active" 
            }, 
            { 
                "name": "###", 
                "state": "Locked" 
            }, 
            { 
                "name": "###", 
                "state": "Active" 
            },
            { 
                "name": "###", 
                "state": "Cleared" 
            },
            { 
                "name": "###", 
                "state": "Cleared" 
            },
            { 
                "name": "###", 
                "state": "Cleared" 
            }
    ]

    oneResponseDict = []
    members=[]
    for i in range (0, len(oneViewList)):
        myToken = returnToken(oneViewList[i]["name"])
        oneResponseDict.append(oneViewStateFunc(oneViewList[i]["name"], oneViewList[i]["state"], myToken)) 
        members.append(oneResponseDict[i]["members"])
    return members
