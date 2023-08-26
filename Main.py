from fakeDictionary import *
from realDictionary import *
from readIncident import *
from createIncident import *
from resolve import *

def mainFunc():
    Debug=True
    if Debug==False:
        newAlertList = realDictionary()  
    else:
        newAlertList = fakeDictionary() # [ { "uri","description","urgency","severity","alertState" }, {}, {} ]

    existIncident = readIncident() # [ {number, short_description, state, sys_id}, {}, {} ]
    incidentList=[] # [ "short_description", "", "" ]
    sysIDlist=[] #[ {"sys_id"}, {}, {}]
    for item in existIncident:
        incidentList.append(item["short_description"])
        sysIDlist.append(item["sys_id"])

    for alert in range (len(newAlertList)):
        uri = newAlertList[alert]["uri"]
        alertID = uri[-5::]
        description = newAlertList[alert]["description"] 
        incidentFound=False  
        for short_description in incidentList:    
            #print(short_description)
            #print(alertID)
            if alertID in short_description:
                #print("match found!")
                if newAlertList[alert]["alertState"] == "Cleared":
                    for sys in sysIDlist:
                        resolveIncident(sys)
                incidentFound=True
                break
        if (incidentFound==False):
            #print("creating {}".format(alertID))
            createIncident(uri, alertID, description)