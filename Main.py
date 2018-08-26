# Xavier Collantes
# 08/25/18
# Examples tried out from Al Sweigart's book, "Automating the Boring Stuff with Python"
# Web Scraping: Chapter 11

import webbrowser, sys, pyperclip, requests

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
	
	
def scrape():
	linkAli = "https://www.gutenberg.org/files/1009/1009-8.txt"
	
	try:
		response = requests.get(linkAli)
		response.raise_for_status()
		
	except Exception as e:
		print("Problem connecting: %s" % e)
		
	print (response.text[1050:1500])
		
if __name__ == "__main__":
	program = sys.argv[1]
	defList = {'mapIt':mapIt, 'scrape':scrape}
	
	for k, v in defList.items():
		if k.upper() == program.upper():
			v()