# Xavier Collantes
# 08/25/18
# Examples tried out from Al Sweigart's book, "Automating the Boring Stuff with Python"
# Web Scraping: Chapter 11

import webbrowser, sys, pyperclip, requests, pprint, os, bs4

# Launches Google Maps in browser from command line argument 
# or clipboard if no command line argument found. 

def mapIt():
	if len(sys.argv) > 2:
		address = ' '.join(sys.argv[2:])
		
	else:
		print ("From clipboard")
		address = pyperclip.paste()
	
	print(address)
	print(type(address))
	linkMap = "https://www.google.com/maps/place/" + address
	webbrowser.open(linkMap)
	

def toFile():
	linkFed = "https://www.gutenberg.org/files/1404/1404-8.txt"
	Fpath = "./lib/fed_papers.txt"
	Dpath = "./lib/"
	chunkSize = 100000
	
	if not os.path.exists(Dpath):
		print("Error with finding destination file.  Creating path... ")
		os.makedirs(Dpath)
	
	try:
		response = requests.get(linkFed)
		response.raise_for_status()
	except Exception as e:
		print ("Error loading file: %s" % e)
	
	try:
		file = open(Fpath, 'wb')
		chunkCount = 0
		bookLength = 0
		for chunk in response.iter_content(chunkSize):
			print (chunk)
			
			file.write(chunk)
			chunkCount += 1
			bookLength += len(chunk)
			print("CHUNK COUNT: %s" %chunkCount)
			print("CHAR LEN: %s" % bookLength)
			print("PER CHUNK: %s" %(bookLength/chunkCount))
	except IOError as ioe:
		print("Error writing to file: %s" % ioe)

	file.close()
	
	
def scrape():
	linkAli = "https://www.gutenberg.org/files/1009/1009-8.txt"
	
	try:
		response = requests.get(linkAli)
		response.raise_for_status()
		
	except Exception as e:
		print("Problem connecting: %s" % e)
		
	print (response.text[1050:1500])

	
def getHTML():
	linkSoup = "https://xaviercollantes.me"
	
	try:
		response = requests.get(linkSoup)
		response.raise_for_status()
		Soup = bs4.BeautifulSoup(response.text)
	except Exception as e:
		print("Uh-oh! Error parsing HTML page: %s" % e)
		
	elems = Soup.select('div')
	
	#print(elems[20])
	print(elems[20].attrs)
	#print(elems[20].getText())
	
	
if __name__ == "__main__":
	defList = {'mapIt':mapIt, 'toFile':toFile, 'scrape':scrape, 'getHTML':getHTML}
	
	try:
		program = sys.argv[1]	
		for k, v in defList.items():
			if k.upper() == program.upper():
				v()
		
	except IndexError as e:
		print("No program named.  Please name one of the following: ")
		print(defList.keys())