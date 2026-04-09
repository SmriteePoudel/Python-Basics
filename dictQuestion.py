user_info = {
    "name":"Hari",
    "phone":[
        {
            "type":"NTC",
            "number":"9844"
        },
        {
            "type":"NCELL",
            "number":"980"
        }
    ]
}

# output
'''
Hari NCELL number is 980
Hari NTC number is 9844
 

'''
user_info = {
    "name": "Hari",
    "phone": [
        {
            "type": "NTC",
            "number": "9844"
        },
        {
            "type": "NCELL",
            "number": "980"
        }
    ]
}

print(f"{user_info['name']} {user_info['phone'][1]['type']} number is {user_info['phone'][1]['number']}")
print(f"{user_info['name']} {user_info['phone'][0]['type']} number is {user_info['phone'][0]['number']}")