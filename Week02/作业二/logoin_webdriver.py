#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
import time


def Login(user, paw):
    u'''登录'''
    driver.get("https://processon.com/")
    time.sleep(1)
    # body > header > ul > li:nth-child(5) > a
    driver.find_element_by_xpath("/html/body/header/ul/li[5]/a").click()
    # driver.find_element_by_css_selector("body > header > ul > li:nth-child(5) > a").click()
    driver.find_element_by_id("login_email").clear()
    driver.find_element_by_id("login_password").clear()
    time.sleep(2)
    driver.find_element_by_id("login_email").send_keys(user)
    driver.find_element_by_id("login_password").send_keys(paw)
    time.sleep(2)
    driver.find_element_by_id("signin_btn").click()
    # driver.find_element_by_xpath(".//*[@id='loginbox']/div/div[2]/form/div[4]/div/div/input").click()
    driver.maximize_window()
    return driver


if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        driver = Login("1377068752----", "qa---")
        t= driver.find_element_by_link_text("帮助手册").text
    # 判断是否登录成功
        # print(t)
        if t == "帮助手册":
            print("登录成功")
        else:
            print("登录失败")
    except Exception as e:
        print(e)
    finally:
        driver.close()

    