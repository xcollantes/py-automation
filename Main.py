# Xavier Collantes
# 08/25/18
# Examples tried out from Al Sweigart's book, "Automating the Boring Stuff with Python"
# Web Scraping: Chapter 11

import webbrowser, sys, pyperclip 

# Launches Google Maps in browser from command line argument 
# or clipboard if no command line argument found. 

def mapIt():
	if len(sys.argv) > 2:
		address = ' '.join(sys.argv[1:])
		
	else:
		print ("From clipboard")
		address = pyperclip.paste()
	
	print(address)
	print(type(address))
	link = "https://www.google.com/maps/place/" + address
	webbrowser.open(link)
	
	
if __name__ == "__main__":
	mapIt()