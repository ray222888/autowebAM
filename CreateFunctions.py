#!/usr/bin/python
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as chains
from selenium.webdriver.common.keys import Keys

def find(driver,str):
    element= driver.find_element_by_xpath("//button[text()='"+str.capitalize()+"']")
    if element:
        return element
    else:
        return False

def fill_from(object,strAction):
    print("fill form")
    browser = object
    listinput=[]

   

    try:
        dropdownbox= browser.find_element_by_css_selector("#clearing-house-dropdown-menu-button")
        dropdownbox.click()
        sleep(5)
        dropdownboxitems= browser.find_element_by_css_selector("#participant-info-section > div:nth-child(1) > div > div.clearing-house.selector.show.open > div > a:nth-child(1)")
        dropdownboxitems.click()
    except:
        print('dropdownbox error')

    selects= browser.find_elements_by_tag_name("select")
    print('len(selects)')
    print(len(selects))
    for arg in selects[0:]:
        try:
            Select(arg).select_by_index(1)
        except:
            print('Select error')

    labels= browser.find_elements_by_tag_name("label")
    print ('len(labels)')
    print (len(labels))

    for arg in labels[0:]:
      try:
          arg.click()
      except:
        print('labels')

    es= browser.find_elements_by_tag_name("input")
    print ('len(input)')
    print (len(es))

    for arg in es[0:]:
        try:
         if (arg.get_attribute('value') != ''):
            print(arg.get_attribute('value'))
            continue
        except Exception as argx:
         print(argx)
        if ((arg.get_attribute('placeholder') == 'Type your answer here...'  ) and ((arg.get_attribute('aria-label') == 'Email Address' ) or (arg.get_attribute('type') == 'email'))):
            try:
             arg.send_keys('test@epam.com')
             listinput.append('test@epam.com')
            except:
                print(arg)
        elif (arg.get_attribute('placeholder') == 'Type your answer here...'  ) and (arg.get_attribute('maxlength') == '50' ):
            try:
              arg.send_keys('cctest@epam.com')
              #listinput.append('cctest@epam.com')
            except:
                print(arg)
        elif ((arg.get_attribute('placeholder') == 'Type your answer here...') or (arg.get_attribute('placeholder') == 'Type telephone number here...')) and ((arg.get_attribute('aria-label') == 'Telephone Number') or (arg.get_attribute('aria-labelledby') == 'guideContainer-rootPanel-contactInformation-contactPersons-contact-phone___guideFieldShortDescription')):
            try:
             arg.send_keys('123-1234-1234')
             listinput.append('123-1234-1234')
            except:
                print(arg)
        elif (arg.get_attribute('placeholder') == 'Type your answer here...') and (arg.get_attribute('aria-labelledby') == 'guideContainer-rootPanel-contactinformationse-contactInformationFragment-confirmationDetailsWrapper-loginuserid___guideFieldShortDescription'):
                try:
                    arg.send_keys('BO_C88888')
                    listinput.append('BO_C88888')
                except:
                    print(arg)
        elif (arg.get_attribute('placeholder') == 'dd-mmm-yyyy') or (arg.get_attribute('placeholder') == 'dd-mmm-yy'):
                try:
                    arg.send_keys((datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%d-%b-%Y"))
                    listinput.append((datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%d-%b-%Y").lower())
                except:
                    print(arg)
        elif (arg.get_attribute('placeholder') == 'dd-mmm-yy'):
                try:
                    arg.send_keys((datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%d-%b-%y"))
                    listinput.append((datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%d-%b-%Y").lower())
                except:
                    print(arg)
        elif (arg.get_attribute('aria-label') == 'Stock Code'):
            try:
                arg.send_keys(600)
                sleep(3)
                menu=browser.find_element_by_xpath("//*[@id=\"guideContainer-rootPanel-detailsOfFailedDeliveryPositionSection-detailsOfFailedDeliveryPositionFragment-stockCode__\"]/table/tbody/tr/td[2]")
                actions = chains(browser)
                #actions.move_to_element(menu)
                #sleep(3)
                actions.move_to_element(menu).click().perform()
                listinput.append(600)
            except Exception as e: print(e)
        elif (arg.get_attribute('aria-label') == 'Stock Name'):
            try:
                #arg.send_keys('CHINA INFRASTRUCTURE INVESTMENT LIMITED')
                listinput.append('CHINA INFRASTRUCTURE INVESTMENT LIMITED')
            except:
                print(arg)
        elif (arg.get_attribute('aria-labelledby') == 'guideContainer-rootPanel-detailsOfFailedDeliveryPositionSection-detailsOfFailedDeliveryPositionFragment-settlementPosNo___guideFieldShortDescription'):
            try:
                arg.send_keys('P12345678')
                listinput.append('P12345678')
            except:
                print(arg)
        elif (arg.get_attribute('aria-labelledby') == 'guideContainer-rootPanel-detailsOfFailedDeliveryPositionSection-detailsOfFailedDeliveryPositionFragment-shareQuantityApplied___guideFieldShortDescription'):
            try:
                arg.send_keys('12345678')
                listinput.append('12345678')
            except:
                print(arg)        
        elif (arg.get_attribute('placeholder') == 'Type your answer here...'  ):
            try:
                #numberrx =random.randint(12345678901234567890,123456789012345678901234567890)
                arg.send_keys("12345678")
                listinput.append(arg.get_attribute('value'))
            except Exception as exa:
                print(exa)
        else:
            try:
             arg.send_keys('1')
            except:
                print(arg)
                
    textareas= browser.find_elements_by_tag_name("textarea")
    print ('len(textareas)')
    print (len(textareas))
    for arg in textareas[0:]:
        try:
         arg.send_keys('abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij')
         listinput.append(arg.get_attribute('value'))
        except:
         print('textareas error')

    selects= browser.find_elements_by_tag_name("select")
    print('len(selects)')
    print(len(selects))
    for arg in selects[0:]:
        try:
            Select(arg).select_by_index(1)
        except:
            print('Select error')       
            
    for arg in es[0:]:
        try:
         print(arg.get_attribute('aria-selected'))
         if arg.get_attribute('aria-selected') == 'true':
                listinput.append(arg.get_attribute('aria-label').lower())
                print(arg.get_attribute('value'))
        except:
              print('radio')
    print(listinput)


    try:
        browser.find_element_by_id("preview-btn").click()
        sleep(3)
        browser.find_element_by_id("preview-btn").click()
        sleep(3)
        browser.find_element_by_id("preview-btn").click()
        sleep(5)
    except:
        print('preview error')

    try: 
        buttons= browser.find_element_by_xpath("//button[text()='"+strAction.capitalize()+"']")
        buttons.click()
        sleep(3)
        vbuttons=browser.find_element_by_xpath("//button[text()='"+strAction.capitalize()+"']")
        vbuttons.click()
        sleep(3)
    except:
       print('action error '+strAction)    
    handles = browser.window_handles
    browser.switch_to.window(handles[0])
    try:
     browser.find_element_by_id("message-text").send_keys(strAction)
     browser.find_element_by_css_selector("div.modal-footer > button:nth-child(2)").click()
    except:
     print("cant click")
     return 'error'
    sleep(15)
    return listinput

def login_from(object,username,password):
    browser=object
    sleep(15)
    try:
     user=browser.find_element_by_css_selector('#idToken1');
     user.send_keys(username);
     userpas=browser.find_element_by_css_selector('#idToken2');
     userpas.send_keys(password);
     sleep(2)
     userpas.send_keys(Keys.ENTER)
     userpasbutton=browser.find_element_by_id('loginButton_0');

     userpasbutton.click();
     sleep(15)
    except Exception as ex:
        print (ex)
        return 'error'

