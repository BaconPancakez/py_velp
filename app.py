import requests
from config import api_key

url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "term": "barber",
    "location": "NYC"

}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

for business in businesses:
    print(business['name'])

name = [business['name']
        for business in businesses if business['rating'] > 4.5]
print(name)
