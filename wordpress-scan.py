import urllib.request
import urllib.parse
#created by ghost0-1(my idea)
#free tools for all
#no copyright
#ssl bypass code from :http://community.netapp.com/t5/Software-Development-Kit-SDK-and-API-Discussions/Python-How-to-disable-SSL-certificate-verification/td-p/113697
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
#function for all action
#wpscan v1
def wpscan(site):
	#opening the url:
	open_url = urllib.request.urlopen(site)
	#debug-log
	debug = site+"/debug.log"
	print("##########################################")
	print("debug file:\n")
	try:
		open_url = urllib.request.urlopen(debug)
		print(str("debug.log exist -->"+open_url))
	except urllib.error.HTTPError as ce:
		print("#error code response:")
		print(str(ce))
	#wp-config-php
	print("##########################################")
	print("wp-config backup:\n")
	backups = ['wp-config.php~','wp-config.php.old','wp-config.php.txt']
	for i in backups:
		config = site+"/"+i
		try:
			open_url = urllib.request.urlopen(config)
			print(str(i+" exist"))
			print("try:"+config+"\n")
		except urllib.error.HTTPError as ce:
			print("#error code response for "+i+":")
			print(str(ce))
	#searchreplacedb2-php
	print("##########################################")
	print("searchreplacedb2:\n")
	srd2 = site+"/searchreplacedb2.php"
	try:
		open_url = urllib.request.urlopen(srd2)
		print(str("searchreplacedb2.php exist -->"+srd2))
	except urllib.error.HTTPError as ce:
		print("#error code response:")
		print(str(ce))
	#emergency-php
	print("##########################################")
	print("emergency:\n")
	emergency = site+"/emergency.php"
	try:
		open_url = urllib.request.urlopen(emergency)
		print(str("emergency.php exist -->"+emergency))
	except urllib.error.HTTPError as ce:
		print("#error code response:")
		print(str(ce))
	#enumeration of username
	print("##########################################")
	print("searching username for "+site+":\n")
	for i in range(1,41):
	    enumerate_ = site+"/?author="+str(i)
	    enumerate_ = urllib.request.urlopen(enumerate_)
	    urlget = enumerate_.geturl()
	    try:
	        if "?author" not in urlget:
                    list_ = urlget.split('/')
                    list_.remove(list_[1])
                    list_.remove(list_[-1])
                    print("username found:"+list_[-1]+"(id="+str(i)+")")
	    except urllib.error.HTTPError as ce:
                print(ce)
    
	print("thank u for using wpscan!!!")
                  
#start function wpscan()
target = input(str("put your target with 'http://'(ex:http://example.com):"))
wpscan(target)
