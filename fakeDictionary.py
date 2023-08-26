#Urgency: ["Immediate", "Low", "Medium", "None", "High","Deferrable"])

def fakeDictionary():
    fake={
        "members": [
            {
                "uri": "/rest/alerts/55555",
                "description": "An unexpected server power off was detected during the firmware update.", 
                "urgency": "Medium", 
                "severity": "Critical",
                "alertState": "Cleared"
            },
            {
                "uri": "/rest/alerts/66666",
                "description": "The embedded flash device on the server has failed the iLO diagnostic self-test.", 
                "urgency": "Immediate",
                "severity": "Critical",
                "alertState": "Locked"
            },
            {
                "uri": "/rest/alerts/77777",
                "description": "One or more devices are not properly connected for remote support.", 
                "urgency": "Low", 
                "severity": "Critical",
                "alertState": "Cleared"
            },
            {
                "uri": "/rest/alerts/88888",
                "description": "The embedded flash device on the server has failed the iLO diagnostic self-test.", 
                "urgency": "Immediate",
                "severity": "Critical",
                "alertState": "Active"
            },
            {
                "uri": "/rest/alerts/99999",
                "description": "One or more devices are not properly connected for remote support.", 
                "urgency": "Low", 
                "severity": "Critical",
                "alertState": "Locked"
            }
        ],
    } 
    return fake["members"]
