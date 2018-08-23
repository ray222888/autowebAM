#!/usr/bin/python
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
import FillForm
import ReadExcel
import clientSend
from unittest import TestCase
from selenium.webdriver.ie.options import Options
import sys

users = 'users.xls'
cases = '1cases.xls'
try:
 if (sys.argv[1] !=''):
  cases = sys.argv[1]
except Exception as ex: print(ex)

UPlist =ReadExcel.readUsers(users)
print(UPlist)
casesList=ReadExcel.readCases(cases)
print(casesList)
caserow=0

for arg in casesList[0:]:
 caserow = caserow+1  
 datalist =arg.split(',')
 datalist.remove('')
 url=''
 step=1
 for arg in datalist[1:]:
     global listinput1
     browser = webdriver.Chrome()

     #ie_driver = r'\IEDriverServer.exe'
     #opts = Options()
     #opts.ignore_protected_mode_settings = True
     #opts.ignore_zoom_level = True
     #opts.require_window_focus = True
     #browser = webdriver.Ie(ie_driver, ie_options=opts)
     try:
      browser.maximize_window()
      browser.implicitly_wait(2)
     except Exception as ex: 
         print(ex)
     #split data ,
     browser.get(datalist[0])

     eventdatalist =arg.split(':')

     try:
      if eventdatalist[0]=='user1':
        eventdatalist[0]=UPlist[1]
      elif eventdatalist[0]=='user2':
        eventdatalist[0]=UPlist[2]
      elif eventdatalist[0]=='user3':
        eventdatalist[0]=UPlist[3]
      elif eventdatalist[0]=='user4':
        eventdatalist[0]=UPlist[4]
      elif eventdatalist[0]=='user5':
        eventdatalist[0]=UPlist[5]
      elif eventdatalist[0]=='user6':
          eventdatalist[0]=UPlist[6]
     except:
      print('user file error')

     logininput=FillForm.login_from(browser,eventdatalist[0],UPlist[0])
     if logininput == 'error':
       browser.get_screenshot_as_file(str(caserow)+'.png')
       ReadExcel.excelUpdate(cases+":Fail,"+str(caserow)+'.png:'+str(caserow))
       clientSend.resultSend(cases+":Fail,"+str(caserow)+'.png:'+str(caserow))
       break


     try:
      browser.get(datalist[0])
      browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))

      try:
          browser.find_element_by_id("claim-btn").click()
          sleep(3)
          browser.find_element_by_id("claim-btn").click()
          sleep(5)
      except:
         print('claim error')
      
      expandbutton=browser.find_element_by_css_selector('#guideContainer-rootPanel-readOnlyInformation-collapseButtons___guide-item > div');
      expandbutton.click()
     except:
      print('expandbutton')
     
    # result1=FormValidation.from_contain(browser,eventdatalist[0])
    # if result1 == 'true':
     # print("pass")
     #else:
      #   print(result1)
     #    break
         
    # if step>0:
     #    result1=FormValidation.from_value(browser,listinput1,cases,caserow,eventdatalist[1])
      #   if result1 == 'true':
       #      print("pass")
        # else:
         #    print(result1)
          #   break    

     listinput1=FillForm.fill_from(browser,eventdatalist[1])
     if listinput1 == 'error':
        browser.get_screenshot_as_file(str(caserow)+'.png')
        ReadExcel.excelUpdate(cases+":Fail,"+str(caserow)+'.png:'+str(caserow))
        clientSend.resultSend(cases+":Fail,"+str(caserow)+'.png:'+str(caserow))
        break
     else:
         ReadExcel.excelUpdate(cases+":Pass:"+str(caserow))
         browser.get_screenshot_as_file(str(caserow)+"_"+str(step)+'.png')
         if (step==len(datalist)):
             clientSend.resultSend(cases+":Pass:"+str(caserow))
     #validate after preview,last submit
     #FormValidation.from_value(browser,listinput,cases,caserow,eventdatalist[1])
     url = browser.current_url
     print(url)
     step=step+1
     browser.quit()
#add send email when finish





