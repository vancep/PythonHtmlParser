import urllib.request
import sys
import getopt

def ParseText(text):
	parsed = ""
	
	# discard everything between <'s and >'s
	i = 0
	while(i < len(text)):
		if (text[i] == '<'):
			while(i < len(text) and text[i] != '>'):
				i += 1
		else:
			parsed += text[i]

		i += 1
		
	#print(text, "\n\nEnd of Originial Text\n")
	print(parsed, "\n\nEnd of Parsed Text")
	
def main(website):
	print("Website: ", website, "\n")
	html = ""
	html = urllib.request.urlopen(website).read()
	ParseText(html.decode(encoding='ascii', errors='ignore'))
	
if(len(sys.argv) > 1):
	main(sys.argv[1])
else:
	print("try: py ParseTextFromSite.py <website>")
