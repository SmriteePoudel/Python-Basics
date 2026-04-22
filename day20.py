# JSON
#Read the json file
import json 
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)


#Write to a json file
with open('data.json','w') as file:
    json.dump(data, file,indent=4)