from bs4 import BeautifulSoup
import dryscrape

url = "https://who.sprinklr.com/"
sess = dryscrape.Session()
sess.visit(url)
content = BeautifulSoup(sess.body(), "html.parser")
finalData = []
print(content)
