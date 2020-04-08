from bs4 import BeautifulSoup
import dryscrape

url = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
sess = dryscrape.Session()
sess.visit(url)
content = BeautifulSoup(sess.body(), "html.parser")
print(content)
