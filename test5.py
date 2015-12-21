# -*- coding: utf-8 -*-
import time
from splinter import Browser

def splinter(url):
    #name = raw_input('username：')
    #pwd = raw_input('pwd：')
    browser = Browser()
    # login 126 email
    browser.visit(url)
    #raw_input("Please <enter>")
    # wait web element loading
    #time.sleep(1)
    # fill in account and password
    #browser.find_by_id('idInput').fill(name)
    #browser.find_by_id('pwdInput').fill(pwd)
    # click the button of login
    #browser.find_by_id('loginBtn').click()
    #time.sleep(1)
    # close the window of
    #browser.quit()

if __name__ == '__main__':
    splinter('http://www.126.com')
    #time.sleep(1)
    #print raw_input("Please <enter>")
