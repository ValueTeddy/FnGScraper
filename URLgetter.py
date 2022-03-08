import requests
# Searches for URLS and puts them into a file
# Replace com,cnn,money)/data/fear-and-greed with https://web.archive.org/
# Add / between numbers and https://money
# Remove whitespaces
# Remove any :80
# Remove html responses that are not 200
# Remove anything after https://money.cnn.com/data/fear-and-greed/
# Final format should be "https://web.archive.org/20211125022427/https://money.cnn.com/data/fear-and-greed/"

data = requests.get("http://web.archive.org/cdx/search/cdx?url=https://money.cnn.com/data/fear-and-greed/")

with open ("\output\URLgetter\URLoutput.txt","w") as outfile:
    outfile.write(data.text)