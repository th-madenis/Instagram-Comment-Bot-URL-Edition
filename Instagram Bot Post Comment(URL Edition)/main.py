import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver import Firefox

# Firefox Profile setting up (configuration setup)
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile() #Load Firefox Profiler
profile.set_preference("general.useragent.override", user_agent) #Set new user agent for the firefox profiler
profile.set_preference("browser.privatebrowsing.autostart", True) #Turn on icognito
driver = webdriver.Firefox(profile) #Load the firefox config and start a new browser tab session
driver.set_window_size(500, 950) #Set the display/window size for the browser tab
#End of setup config firefox, let's start




driver.get("-----------------------------------") #Go to this url


delay = 6 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'body'))) #Lets wait for the page to load
    print("Page is ready!")
    try:
        cookie_modal_acception = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html.js.not-logged-in.client-root.touch.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.FrS-d'))) #Lets wait for the page to load
        print("Cookie Modal Acception fuck us, lets shoot it")
        accept_cookie_btn = driver.find_element_by_css_selector('html.js.not-logged-in.client-root.touch.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.FrS-d div._1XyCr div.piCib div.mt3GC button.aOOlW.bIiDR') #Find this html element in the page
        accept_cookie_btn.click() #Click the button
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html.js.not-logged-in.client-root.touch.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.uzKWK div.Igw0E._56XdI.YBx95.ybXk5._4EzTm.i0EQd div.rgFsT.M2tlr div.gr27e div.EPjEi form#loginForm.HmktE'))) #Lets wait for the page to load
            print("Login Form Detected!")
            username_field = driver.find_element_by_xpath('/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[3]/div/label/input') #Find the login username field
            password_field = driver.find_element_by_xpath('/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[4]/div/label/input') #Find the login password field
            username_field.send_keys("----------------") #Give your email
            time.sleep(2) #Wait  
            password_field.send_keys("----------") #Give your password
            time.sleep(2) #Wait
            login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[6]') #Find the login button
            login_btn.click() # Click login
            time.sleep(6)
            driver.get("https://www.instagram.com/p/CIRG1D6lTvO/") 
            try:
                WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html.js.logged-in.client-root.touch.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.uzKWK div.Kj7h1 div.ltEKP article.QBXjJ.M9sTE.h0YNM.SgTZ1 div.eo2As'))) #Lets wait for the page to load
                comment_btn = driver.find_element_by_css_selector('html.js.logged-in.client-root.touch.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T main.SCxLW.uzKWK div.Kj7h1 div.ltEKP article.QBXjJ.M9sTE.h0YNM.SgTZ1 div.eo2As section.ltpMr.Slqrh span._15y0l button.wpO6b')
                comment_btn.click()
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/section/div/form')))
                    comment_box_txt = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/form/textarea')
                    comment_box_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/form/button')
                    arithmos = 0
                    while arithmos <= 10:
                        comment_box_txt.send_keys("@madenis @ {}".format(str(arithmos)))
                        comment_box_btn.click()
                        arithmos += 1
                        time.sleep(2)
                    driver.close()   #Close the window and stop the programm
                except:
                    print("I can't see the comment dialog")
            except:
                print("I can't find the post action buttons")
        except:
            print("We dont find any login form to continue")
    except:
        print("We can continue our life!")
except:
    print("Loading took too much time!")
