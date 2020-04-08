from bs4 import BeautifulSoup
import requests
import json

url = "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html"
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")
finalData = []
for _,data in enumerate(content('li')):
    if data.string is not None:
        if data.string.startswith('Total'):
            finalData.append(data.string)
        if data.string.startswith('Jurisdictions'):
            finalData.append(data.string)
print(json.dumps(finalData))
