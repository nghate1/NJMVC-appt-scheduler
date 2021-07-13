import urllib.request
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import winsound

firstName = 'Aayush'
lastName = 'Sharma'
email = 'nickinnj44@gmail.com'
phone = '7328232950'
birthday = '04/29/2002'

locations = ['197', '186']

def beep():
    winsound.Beep(1500, 500)
    winsound.Beep(4500, 500)
    winsound.Beep(2500, 500)
    winsound.Beep(1500, 500)
    winsound.Beep(4500, 500)
    winsound.Beep(2500, 500)

def fillForm():
    web = webdriver.Firefox()
    web.get('https://telegov.njportal.com/njmvc/AppointmentWizard/15')
    makeAppt = web.find_element_by_xpath('//*[@id="makebtn19715"]')
    makeAppt.click()

    apptTime = web.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div/div[3]/div/div[2]/div/a/div')
    apptTime.click()

    first = web.find_element_by_xpath('//*[@id="firstName"]')
    first.send_keys(firstName)

    last = web.find_element_by_xpath('//*[@id="lastName"]')
    last.send_keys(lastName)

    e = web.find_element_by_xpath('//*[@id="email"]')
    e.send_keys(email)

    p = web.find_element_by_xpath('//*[@id="phone"]')
    p.send_keys(phone)

    ptype = web.find_element_by_xpath('//*[@id="permitType"]')
    ptype.click()

    pselect = web.find_element_by_xpath('/html/body/main/div/form/div[1]/div/div[5]/div/div[3]/div[1]/div/select/option[6]')
    pselect.click()

    dob = web.find_element_by_xpath('//*[@id="birthDate"]')
    dob.send_keys(birthday)

    conf = web.find_element_by_xpath('//*[@id="receiveTexts"]')
    conf.click()

    submit = web.find_element_by_xpath('/html/body/main/div/form/div[1]/div/div[5]/div/div[6]/div[1]/input')
    submit.click()

def job():
    site = urllib.request.urlopen('https://telegov.njportal.com/njmvc/AppointmentWizard/15/')
    html_source = site.read()
    encoding = 'utf-8'
    html_source = html_source.decode(encoding)

    for location in locations:
        #cut out the specific string we want
        html_source = html_source[html_source.index("{\"LocationId\":"+location+",\"FirstOpenSlot\":")+len("{\"LocationId\":"+location+",\"FirstOpenSlot\":"):html_source.index("\"LocationId\":"+str(int(location)+1)+",\"FirstOpenSlot\":")]
        html_source = html_source[html_source.index("Next Available: ")+len("Next Available: "):html_source.index("\"},{")]
        month = int(html_source[0:2])
        date = int(html_source[3:5])
        print(month)
        print(date)
        if (month == 6):
            beep()
            fillForm()

while True :
    try:
        job()
    except:
        print("Something went wrong")
        time.sleep(30)
    else:
        time.sleep(30)
    
