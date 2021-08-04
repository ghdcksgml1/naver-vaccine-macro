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
trigger = 0
prev = ""


def ready(E1,E2,E3,Chr_Folder):
    global driver
    try:
        driver = webdriver.Chrome(Chr_Folder)
    except:
        print("크롬 드라이버 경로가 정확하지 않은 것 같습니다.\n 프로그램을 재시작해서 정확한 chromedriver를 선택해주세요.\n 버전 꼭 확인요망")
        return
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
    try:
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
            if(trigger >= 300):
                trigger=0
                for i in range(0,3):
                    driver.switch_to_window(driver.window_handles[i])
                    driver.get_window_position(driver.window_handles[i])
                    driver.refresh()
                time.sleep(1)
    except:
        print("창이 아직 켜져있지 않습니다. 준비를 눌러 세팅하세요.")
        return

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
    try:
        prev = ""
        trigger = 0
        driver.switch_to_window(driver.window_handles[0])
        driver.get_window_position(driver.window_handles[0])
    except:
        print("창이 닫혀있는 것 같습니다. 준비를 눌러 다시 창을 켜주세요.")

