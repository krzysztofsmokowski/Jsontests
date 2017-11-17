import json
with open('aws.json') as json_data:
    data = json.load(json_data)
json = data
'''iteration responsible for iterating through json in search of InstanceId'''
for reservations in json["Reservations"]:
    for instance in reservations['Instances']:
        if instance['State']['Name'] == 'running':
            print(instance['InstanceId'])

