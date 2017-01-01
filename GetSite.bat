SET myWebsite=https://www.washingtonpost.com
SET myOutputFile=SiteHTML.txt

py ParseTextFromSite.py %myWebsite% > %myOutputFile%

chcp

pause