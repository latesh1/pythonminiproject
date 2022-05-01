import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"India"}

headers = {
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com",
	"X-RapidAPI-Key": "13c2463fb4msh6f93401f95bd498p192bfajsn67815cb11a2f"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response1=response.json()


# with open('covidapi.json','w') as file:
#     json.dump(response1,file)


l1=response1['response'][0]['cases']['active']
l2=response1['response'][0]['cases']['recovered']
