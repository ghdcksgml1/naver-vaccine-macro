from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from tkinter import *
from tkinter import filedialog as fd
import tkinter.font as tkFont
import time

driver = ""
Chr_Folder = ""
trigger = 0
prev =""

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def ready():
    global driver
    driver=webdriver.Chrome(Chr_Folder)
    driver.get('https://talk.naver.com/')
    driver.maximize_window()

def start():
    global driver
    global prev
    global trigger
    while(True):
        trigger+=1
        print(trigger,"초..\n")
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        divs = soup.find_all('span',{'class':'_time'})
        times = divs[len(divs)-1].text.strip()
        #times[1]에 12:00 저장
        times = times.split()
        if(trigger!=1 and times[1] != prev):
            element = driver.find_elements_by_class_name('btn_basic')
            element[len(element)-2].click()
            break
        else:
            prev = times[1]
    driver.switch_to_window(driver.window_handles[1])
    driver.get_window_position(driver.window_handles[1])
    element3 = driver.find_element_by_xpath(
        '//*[@id="container"]/div/div[2]/div[2]/div/div/label')
    element3.click()
    element4 = driver.find_element_by_id('reservation_confirm')
    element4.click()

def reset():
    global driver
    global prev
    global trigger
    prev=""
    trigger=0
    driver.switch_to_window(driver.window_handles[0])
    driver.get_window_position(driver.window_handles[0])



window = Tk()
window.title("naver_vaccine")
window.geometry("700x500+100+100")
window.resizable(False,False)

FontSize = tkFont.Font(size=30)
r1 = Label(window,text="1. ",font=FontSize).grid(row=1,column=0)
b1 = Button(window, text="준비", command=ready,
            font=FontSize).grid(row=1, column=1)
r2 = Label(window, text="2. ", font=FontSize).grid(row=2, column=0)
b2 = Button(window, text="시작",command=start, font=FontSize).grid(row=2,column=1)
b3 = Button(window,text="리셋",command=reset,font=FontSize).grid(row=4)

Chr_Folder = fd.askopenfilename()

window.mainloop()

