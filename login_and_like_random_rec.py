#!/usr/bin/python
import os
import sys
import subprocess
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException


def main(argv):

    webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept"
	
    login = argv[1]
    password = argv[2]
    page = argv[3]

    ff_prof=webdriver.FirefoxProfile()
    driver = webdriver.Firefox(ff_prof)
    driver.close()
    tor_path = "C:\\Users\\vorop\\Desktop\\Tor Browser\\Browser\\" #tor.exe
    torrc_path = "C:\\Users\\vorop\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Data\\Tor\\torrc"
	
    try:
        #set some privacy settings
        ff_prof.set_preference( "places.history.enabled", False )
        ff_prof.set_preference( "privacy.clearOnShutdown.offlineApps", True )
        ff_prof.set_preference( "privacy.clearOnShutdown.passwords", True )
        ff_prof.set_preference( "privacy.clearOnShutdown.siteSettings", True )
        ff_prof.set_preference( "privacy.sanitize.sanitizeOnShutdown", True )
        ff_prof.set_preference( "signon.rememberSignons", False )
        ff_prof.set_preference( "network.cookie.lifetimePolicy", 2 )
        ff_prof.set_preference( "network.dns.disablePrefetch", True )
        ff_prof.set_preference( "network.http.sendRefererHeader", 0 )
        #set socks proxy
        ff_prof.set_preference( "network.proxy.type", 1 )
        ff_prof.set_preference( "network.proxy.socks_version", 5 )
        ff_prof.set_preference( "network.proxy.socks", '127.0.0.1' )
        ff_prof.set_preference( "network.proxy.socks_port", 9050 )
        ff_prof.set_preference( "network.proxy.socks_remote_dns", True )
        #get a huge speed increase by not downloading images
        #ff_prof.set_preference( "permissions.default.image", 2 )
        DETACHED_PROCESS = 0x00000008
        #calling as a detached_process means the program will not die with your python program - you will need to manually kill it
        ##
        # somebody please let me know if there's a way to make this a child process that automatically dies (in windows)
        ##
        time.sleep(5)
        tor_process = subprocess.Popen( '"' + tor_path+'firefox.exe" --nt-service "-f" " ' + torrc_path + '"' )
        time.sleep(5)
        driver = webdriver.Firefox(ff_prof)
        time.sleep(5)

        #login and like

        driver.get("http://www.livelib.ru")
        driver.find_element_by_class_name("avatar-border").click()

        input = driver.find_element_by_id("form-login-data").find_elements_by_css_selector("input");

        input[1].send_keys(password)
        try:
            str(login)
            input[0].send_keys(login)
            driver.find_element_by_id("user[submit]").click()
            time.sleep(2)
        except UnexpectedAlertPresentException:
            driver.switch_to_alert()
            alert.accept()
            sys.exit()

        time.sleep(7)
        driver.get(page)
        str("logined ")
        elementsByClassName = driver.find_elements_by_class_name("i-vote")
        for item in elementsByClassName:
            item.click()

        driver.find_element_by_class_name("event-user-avatar").click()
        elementsByXpath = driver.find_elements_by_xpath("//*[contains(text(), 'Добавить в друзья')]")
        for item in elementsByXpath:
            item.click()
            alert = driver.switch_to_alert()
            alert.accept()
        time.sleep(5)
        str("success ")
        str(". ")

        driver.close()
        tor_process.kill()
        sys.exit()
    except:
        time.sleep(2)
        tor_process.kill()
        driver.close()
        time.sleep(2)
        sys.exit()
        
if __name__ == "__main__":
    sys.exit(main(sys.argv))
