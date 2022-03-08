from bs4.element import Declaration
import requests
from bs4 import BeautifulSoup
import time
i=0


URL_file_path = r".\URLgetter\URLListcleaned.txt"
Out_file_path = ".\out.txt"

for line in open(URL_file_path, "r"):
    
    URL = line
    print(i)
    i = i+1
    time.sleep(0.5)
    data = requests.get(URL)

    soup = BeautifulSoup(data.text, "html.parser")
    try:
        div = soup.find('div', id="needleChart")
        overtime = soup.find('div', id="feargreedOverTime").prettify()
        date = URL[24:32]

        with open (Out_file_path, "a") as outfile:
            outfile.write("\n"+ date+"\n")
            for li in div.find_all("li"):
                outfile.write(li.text)
                outfile.write("\n")
            outfile.write(overtime)
    except:
        print("error on i: " + str(i))