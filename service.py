import os
import schedule
import time

def job(t,f):
    if f==1:
        os.system("cp /home/yahya/Documents/Daraz-scrapping/proxylist1.txt /home/yahya/Documents/Daraz-scrapping/et")
        os.system("mv /home/yahya/Documents/Daraz-scrapping/et/proxylist1.txt /home/yahya/Documents/Daraz-scrapping/et/proxylist.txt")
        print("Crawling at ",t)
        os.system("scrapy crawl darazscripts")
        os.system("rm /home/yahya/Documents/Daraz-scrapping/et/proxylist.txt")
    else:
        os.system("cp /home/yahya/Documents/Daraz-scrapping/proxylist2.txt /home/yahya/Documents/Daraz-scrapping/et")
        os.system("mv /home/yahya/Documents/Daraz-scrapping/et/proxylist2.txt /home/yahya/Documents/Daraz-scrapping/et/proxylist.txt")
        print("Crawling at ",t)
        os.system("scrapy crawl darazscripts")
        os.system("rm /home/yahya/Documents/Daraz-scrapping/et/proxylist.txt")
    #print("Crawling at ",t)
    #os.system("scrapy crawl darazscripts")
    return
##schedule.every().day.at("01:25").do(job,'It is 01:025',1)      
#chedule.every().day.at("01:25").do(job,'It is 01:025',2)      
schedule.every().day.at("07:00").do(job,'It is 07:00',1)
schedule.every().day.at("07:30").do(job,'It is 07:30',2)
schedule.every().day.at("08:30").do(job,'It is 08:30',1)
schedule.every().day.at("09:00").do(job,'It is 09:00',2)
schedule.every().day.at("10:00").do(job,'It is 10;00',1)
schedule.every().day.at("10:30").do(job,'It is 10:30',2)
schedule.every().day.at("11:00").do(job,'It is 11:00',1)
schedule.every().day.at("12:00").do(job,'It is 12:00',2)
schedule.every().day.at("12:30").do(job,'It is 12:30',1)
schedule.every().day.at("13:16").do(job,'It is 13:16',2)
schedule.every().day.at("13:45").do(job,'It is 13:45',1)
schedule.every().day.at("14:45").do(job,'It is 14:45',2)
schedule.every().day.at("15:15").do(job,'It is 15:15',1)
schedule.every().day.at("16:30").do(job,'It is 16:30',2)
schedule.every().day.at("17:30").do(job,'It is 17:30',1)
schedule.every().day.at("18:00").do(job,'It is 18:00',2)
schedule.every().day.at("19:00").do(job,'It is 19:00',1)
schedule.every().day.at("19:30").do(job,'It is 19:30',2)
schedule.every().day.at("20:33").do(job,'It is 20:33',1)
schedule.every().day.at("21:00").do(job,'It is 21:00',2)
schedule.every().day.at("01:55").do(job,'It is 04:33',2)

while True:
    schedule.run_pending()
    time.sleep(10)
