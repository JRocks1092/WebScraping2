from sqlite3 import Row
from unicodedata import name
from urllib import request
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
tablelist = soup.find_all("table")
table = tablelist[7]

templist = []

for tr in table.find_all("tr"):
    tdList = tr.find_all("td")
    row = [i.text.rstrip() for i in tdList]
    templist.append(row)

names = []
distance = []
mass = []
radius = []

for i in range(1, len(templist)):
    names.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])    

df = pd.DataFrame(list(zip(names, distance, mass, radius)), columns=["Star_Name", "Distance", "Mass", "Radius"])
df.to_csv("DwarfStars.csv")