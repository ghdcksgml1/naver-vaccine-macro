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
prev = ""


def ready():
    global driver
    driver = webdriver.Chrome(Chr_Folder)
    link1 = "https://m.place.naver.com/hospital/"+E1.get()+"/home?entry=pll"
    driver.get(link1)
    time.sleep(0.5)
    link2 = 'window.open("https://m.place.naver.com/hospital/' + \
        E2.get()+'/home?entry=pll");'
    print(link2)
    driver.execute_script(link2)
    time.sleep(0.5)

    link3 = 'window.open("https://m.place.naver.com/hospital/' + \
        E3.get()+'/home?entry=pll");'
    print(link3)
    driver.execute_script(link3)
    time.sleep(0.5)

    driver.maximize_window()


def start():
    global driver
    global prev
    global trigger
    idx = 0
    while(True):
        trigger += 1.3

        idx %= 3
        driver.switch_to_window(driver.window_handles[idx])
        driver.get_window_position(driver.window_handles[idx])
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.select_one('._21J6E')

        if(trigger != 1.3 and divs != prev):
            element = driver.find_element_by_class_name('_21J6E')
            element.click()
            print("Click")
            break
        else:
            print(int(trigger), "초..\n")
            prev = divs
            element2 = driver.find_element_by_class_name('_1N99c')
            element2.click()
            idx += 1
            if(idx == 3):
                time.sleep(1.3)

    # driver.switch_to_window(driver.window_handles[1])
    # driver.get_window_position(driver.window_handles[1])
    time.sleep(0.3)
    try:
        element3 = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[2]/div[2]/div/div/label')
        element3.click()
    except:
        print("동의 버튼이 안눌렸음")

    try:
        element4 = driver.find_element_by_id('reservation_confirm')
        element4.click()
    except:
        print("실패 한듯??.. 리셋 누르고 다시 시작~")


def reset():
    global driver
    global prev
    global trigger
    prev = ""
    trigger = 0
    driver.switch_to_window(driver.window_handles[0])
    driver.get_window_position(driver.window_handles[0])


window = Tk()
window.title("naver_vaccine")
window.geometry("700x500+100+100")
window.resizable(False, False)
rwidth = 10
FontSize = tkFont.Font(size=30)
l1 = Label(window, text="Link 1 : ", font=FontSize).grid(row=1, column=0)
l2 = Label(window, text="Link 2 : ", font=FontSize).grid(row=2, column=0)
l3 = Label(window, text="Link 3 : ", font=FontSize).grid(row=3, column=0)
E1 = Entry(window, width=rwidth)
E1.grid(row=1, column=2)
E2 = Entry(window, width=rwidth)
E2.grid(row=2, column=2)
E3 = Entry(window, width=rwidth)
E3.grid(row=3, column=2)


Chr_Folder = fd.askopenfilename()
b1 = Button(window, text="준비", command=ready, font=FontSize)
b1.grid(row=4, column=0)
b2 = Button(window, text="시작", command=start, font=FontSize)
b2.grid(row=4, column=1)
b3 = Button(window, text="리셋", command=reset, font=FontSize)
b3.grid(row=4, column=2)
window.mainloop()
