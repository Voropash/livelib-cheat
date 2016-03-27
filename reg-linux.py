#!/usr/bin/python
import os
import sys
import subprocess
import random
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys

def main(argv):

    display = Display(visible=0, size=(1024, 768))
    display.start()
    
    login = argv[1]
    password = argv[2]
    name = argv[3]
    image = argv[4]
	
    ff_prof=webdriver.FirefoxProfile()
    driver = webdriver.Firefox(ff_prof)
    driver.close()
    tor_path = "/usr/local/bin/tor-browser" #tor.exe
    torrc_path = "/home/voropash/livelib-py"
    tor_process = subprocess.Popen( 'tor-browser',stdout=subprocess.PIPE)
    tor_process.kill()
	
    while 1:
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
        #DETACHED_PROCESS = 0x00000008
        #calling as a detached_process means the program will not die with your python program - you will need to manually kill it
        ##
        # somebody please let me know if there's a way to make this a child process that automatically dies (in windows)
        ##
        tor_process = subprocess.Popen(tor_path,stdout=subprocess.PIPE)
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
        input[0].send_keys(login)

        #driver.find_element_by_id("register_submit").click()
		
        time.sleep(25)
        #driver.close()
        #tor_process.kill()
        #driver.get("http://www.livelib.ru")
        #driver.find_element_by_class_name("avatar-border").click()
        #input = driver.find_element_by_id("form-login-data").find_elements_by_css_selector("input");
        #input[0].send_keys(login)
        #input[1].send_keys('defPass')
        #driver.find_element_by_id("user[submit]").click()
		
        driver.get("http://www.livelib.ru/account/editprofile")
        driver.find_element_by_id("account[name]").send_keys(name)
        driver.find_element_by_id("account_picture_action_url").click()
        driver.find_element_by_id("account_url").send_keys(image)

        driver.find_element_by_class_name("btn100").click();
            
        driver.get("http://www.livelib.ru/account/rename")
        driver.find_elements_by_class_name("middle")[4].find_element_by_css_selector("input").send_keys(name)
        driver.find_element_by_class_name("btn150").click();
        time.sleep(4)
			
        driver.close()
        tor_process.kill()
        sys.exit()
        
if __name__ == "__main__":
    sys.exit(main(sys.argv))
