from bs4 import BeautifulSoup
import requests
import tabula
import json

url = "https://www.mass.gov/info-details/covid-19-cases-quarantine-and-monitoring#covid-19-cases-in-massachusetts-"
rootURL = "https://www.mass.gov"
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")
template_path = "covid-19-case-report.tabula-template.json"
finalData = []
for _,link in enumerate(content('a')):
    if link.has_attr('href'):
        if link.get('href').endswith('/download'):
            if link.string.startswith('COVID-19 Cases in Massachusetts'):
                r = requests.get(rootURL + link.get('href'))
                with open('COVID_data.pdf', 'wb') as outfile:
                    outfile.write(r.content)
                parsedData = tabula.read_pdf_with_template('COVID_data.pdf', template_path, stream=True)
                for i,table in enumerate(parsedData):
                    table.dropna(inplace=True)
                    table.rename(columns={'Total Patients':'Total Patients Positive'}, inplace=True)
                    table.rename(columns={'Unnamed: 0':'Cases'}, inplace=True)
                    finalData.append(table.to_json(orient='records'))
                print(json.dumps(finalData))