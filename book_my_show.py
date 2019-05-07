import urllib2
from bs4 import BeautifulSoup
import time

final_timings = []

while True:

    time.sleep(5 * 60)

    url = "https://in.bookmyshow.com/buytickets/pokemon-detective-pikachu-hyderabad/movie-hyd-ET00088312-MT/20190511"

    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"})

    response = urllib2.urlopen(req)

    current_url = response.geturl()

    print current_url

    data = response.read()

    s = BeautifulSoup(data, 'html.parser')

    venues = s.find(id="venuelist")

    threshold_time = 0500

    l = venues.find_all("li")

    desired_cinemas = ["AMB Cinemas: Gachibowli",
                    "Platinum Movietime: Gachibowli",
                    "PVR Forum Sujana Mall: Kukatpally, Hyderabad",
                    "PVR ICON: Hitech, Madhapur, Hyderabad",
                    "PVR: Inorbit, Cyberabad",
                    ]

    def send_email(timings):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email = ""
        password = ""
        message = "Hi, there is an update on movie.\n"
        for time in timings:
            message += str(time) + "\n"
        s.login(email, password)
        emails = []
        emails.append("")     #email 1 to send info to
        emails.append("") #email 2 to send info to
        for receiver_email in emails:
            s.sendmail(email, receiver_email, message)
        s.quit()


    if current_url.lower() == url.lower():
        
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
                        print "Checking time"
                        '''if t['data-showtime-code'] >= threshold_time:
                            send_email()'''
                    except:
                        pass
                if len(final_timings) != len(timings):
                    send_email(timings)
                    final_timings = timings
                print timings
                print "\n"