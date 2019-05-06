import urllib2
from bs4 import BeautifulSoup

url = "https://in.bookmyshow.com/buytickets/jersey-hyderabad/movie-hyd-ET00077973-MT/20190506"

req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"})

data = urllib2.urlopen(req).read()

s = BeautifulSoup(data, 'html.parser')

venues = s.find(id="venuelist")

l = venues.find_all("li")

desired_cinemas = ["AMB Cinemas: Gachibowli",
                   "Platinum Movietime: Gachibowli",
                   "PVR Forum Sujana Mall: Kukatpally, Hyderabad",
                   "PVR ICON: Hitech, Madhapur, Hyderabad",
                   "PVR: Inorbit, Cyberabad",
                   ]

for item in l:
    timings = []
    cinema_name = str(item['data-name'])
    if cinema_name in desired_cinemas:
        print "Cinema name: " + cinema_name
        body = item.find_all("div", class_="body")[0]
        times = body.find_all("a")
        for t in times:
            try:
                timings.append(t['data-date-time'])
            except:
                pass
        print timings
        print "\n"
