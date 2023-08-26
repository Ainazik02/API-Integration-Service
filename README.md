# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 



Test 1 - Hello 
# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

If Alerts in OneView > 0:
    Read all Open incidents by assigned_group=CSS, short description = HPE OneView
    If incident for alert exist in SNOW:
        Ignore
    else:
        Create new incident:
            u_external_reference = alert ID,
            comment = Name of Alert + uri, 
            short description = HPE OneView Alert - u_external_reference, 
            category=failure,
            Impact = 2,
            Urgency = 2, 
            
# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

