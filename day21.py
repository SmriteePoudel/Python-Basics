#Api Type
#graphQL- query language for graph databases

#Rest- json based api. 
#soap

import requests


url="https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts/?limit=4"
url = url
r = requests.get(url=url)
if r.status_code == 200:
    print("Successfully fetch")
    result = r.json()
    final= result['data']['news']
    for i in final:
        print("Post id" ,i['post_id'])
        print("------------------------------------------------")
        print("Link",i['link'])
        print("------------------------------------------------")
       
       

else:
    print("No data")






url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=1&from=2025-03-03&to=2025-03-05"

r = requests.get(url=url)
if r.status_code ==200:
 print(r)    

result=r.json() 