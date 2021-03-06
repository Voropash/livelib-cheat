#!/usr/bin/python
import os
import sys
import subprocess
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
import ctypes

def main(argv):

    webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept"
    
    login = argv[1]
    password = argv[2]
    name = argv[3]
    image = argv[4]
	
    ff_prof=webdriver.FirefoxProfile()
    driver = webdriver.Firefox(ff_prof)
    driver.close()
    tor_path = "C:\\Users\\vorop\\Desktop\\Tor Browser\\Browser\\" #tor.exe
    torrc_path = "torrc"
    tor_process = subprocess.Popen( '"' + tor_path+'firefox.exe" --nt-service "-f" "' + torrc_path + '"' )
    tor_process.terminate() 

    
    iterations = 5
    while iterations > 0:
        try:
            try:
                ff_prof=webdriver.FirefoxProfile()
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
                ff_prof.set_preference( "network.proxy.socks_port", 9150 )
                ff_prof.set_preference( "network.proxy.socks_remote_dns", True )
                #get a huge speed increase by not downloading images
                ff_prof.set_preference( "permissions.default.image", 2 )
                # programmatically start tor (in windows environment)
                DETACHED_PROCESS = 0x00000008
                #calling as a detached_process means the program will not die with your python program - you will need to manually kill it
                ##
                # somebody please let me know if there's a way to make this a child process that automatically dies (in windows)
                ##
                tor_process = subprocess.Popen( '"' + tor_path+'firefox.exe"' )
                driver = webdriver.Firefox(ff_prof)
                #registration

                driver.get("http://www.livelib.ru")
                driver.find_element_by_class_name("avatar-border").click()
                driver.find_element_by_class_name("popup-menu").find_elements_by_css_selector("td")[0].click();

                input = driver.find_element_by_id("form-register-data").find_elements_by_css_selector("input");
                            
                            #random.seed()
                            #alphabet = "qwertyuioplkjhgfdsazxcvbnm-";
                            #mail = "";
                            #i = 0
                            #while i<8:
                            #	mail += random.choice(alphabet)
                            #	i = i + 1

                driver.find_element_by_id("reg[agreement]").click()
                            
                input[1].send_keys('defPass')
                try:
                    input[0].send_keys(login)
                    #driver.find_element_by_id("register_submit").click()
                    time.sleep(1)
                    driver.get("http://www.livelib.ru/account/editprofile")
                except UnexpectedAlertPresentException:
                    driver.switch_to_alert()
                    alert.accept()
                    sys.exit()
                break
            except:
                sys.exit()
        except:
            time.sleep(2)
            tor_process.kill()
            driver.close()
            time.sleep(2)
            iterations=iterations-1
            if (iterations < 1):
                sys.exit()

        
    time.sleep(8)
            
    driver.get("http://www.livelib.ru/account/editprofile")
    driver.find_element_by_id("account[name]").send_keys(name)
    driver.find_element_by_id("account[web]").send_keys('http://artMordent.ru')
    driver.find_element_by_id("account_picture_action_url").click()
    driver.find_element_by_id("account_url").send_keys(image)

    driver.find_element_by_class_name("btn100").click();
        
    driver.get("http://www.livelib.ru/account/rename")
    driver.find_elements_by_class_name("middle")[4].find_element_by_css_selector("input").send_keys(name)
    driver.find_element_by_class_name("btn150").click();
    time.sleep(4)
                    
    driver.close()
    tor_process.kill()
        
if __name__ == "__main__":
    sys.exit(main(sys.argv))
