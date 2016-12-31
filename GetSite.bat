SET myWebsite=https://www.google.com
SET myOutputFile=SiteHTML.txt

py ParseTextFromSite.py %myWebsite% > %myOutputFile%

pause