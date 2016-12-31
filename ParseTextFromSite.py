import urllib.request
import sys
import getopt

def ParseText(text):
	parsed = ""
	
	# discard everything between <'s and >'s
	for i in range(len(text)):
		if (text[i] == '<'):
			while(i < len(text) and text[i] != '>'):
				i += 1
		else:
			parsed += chr(text[i])

	print(text, "\n\nEnd of Originial Text\n")
	print(parsed, "\n\nEnd of Parsed Text")
	
def main(website):
	print("Website: ", website)
	response = urllib.request.urlopen(website)
	html = response.read()
	
	ParseText(html)
	
if(len(sys.argv) > 1):
	main(sys.argv[1])
else:
	print("try: py ParseTextFromSite.py <website>")