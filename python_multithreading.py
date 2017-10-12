from multiprocessing import Pool
from collections import defaultdict
from socket import AF_INET
from urllib2 import urlopen
import urllib2
import ssl
import csv
import socket


def filewrite(url,text):
    with open("mgmt1.csv", "a+") as text_file:
              text_file.write(url + "=" + str(text[17:28]) + '\n')

def process_line(line):
    url= "https://" + line.rstrip() + "/public/cimc.esp"
    return url


# Asynchronous request
def async_reqest(url):
    try:
        #print url
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        request = urllib2.Request(url)
        response = urllib2.urlopen(request,context=ctx,timeout=20)
        the_page = response.read()
        if "fwVersion" in the_page:
         with open("mgmt2.csv", "a+") as text_file:
              text_file.write(response.geturl() + "=" + str(the_page[16:28]) + '\n')


    except IOError, e:
        if hasattr(e, 'code'): # HTTPError
         #print 'http error code: ', e.code
         pass
        elif hasattr(e, 'reason'): # URLError
         #print "can't connect, reason: ", e.reason
         pass
        else:
         pass

if __name__ == "__main__":
    pool = Pool(4)
    with open('cicmip.txt') as source_file:
        # chunk the work into batches of 4 lines at a time
        results = pool.map(process_line, source_file, 4)
        p = Pool(10)
        p.map(async_reqest,results)
