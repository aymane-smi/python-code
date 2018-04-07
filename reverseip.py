#importing modules
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#kill it
vic = str(input("enter ur vic: "))
api = "http://api.hackertarget.com/reverseiplookup/?q="+vic
openurl = urllib.request.urlopen(api)
content = (openurl.read(10000))
soup = BeautifulSoup(content,"html.parser")
x = soup.prettify() 
file = open("sites.txt","w+")
file.write(x)
#new_site = urllib.parse.urljoin("http://" , x)
#print(new_site)
file.close()
#adding "http" to url
foo = open("sites.txt","r+")
listt = list(foo.readlines())
def refile():
	for i in listt:
		y = "http://"+i
		y = y.rstrip("\n")
		print(y)
refile()
