from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import json
domain="xyz"#Give the domian name
url="http://xyz.com"#Enter the Domain url
page=urlopen(url)
page_soup=soup(page,"html.parser")
for script in page_soup(["script", "style"]):
        script.decompose()
text = page_soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)
links=page_soup.find_all("a")
leaves=[link.get("href") for link in links]
container = {}
container["domain"] = domain
container["url"] = url
container["leaves"] = leaves
container["links"]=leaves[0]
container["content"] = text.split('\n')
print(container)
f=open("newfile.txt",'w')
f.write(json.dumps([container],indent=8))
