import paramiko
from multiprocessing import Pool
from collections import defaultdict
from socket import AF_INET
from urllib2 import urlopen
import urllib2
import ssl
import csv
import socket



def process_line(line):
    url= line.rstrip()
    return url

# Asynchronous request
def async_reqest(url):
    try:
    	x=str(url).strip()
    	#print x
    	if x == "10.79.131.199":
    		print "true"
        paramiko.Transport._preferred_ciphers = ('diffie-hellman-group1-sha1', 'aes128-ctr','aes192-ctr','aes256-ctr','aes128-cbc','blowfish-cbc','aes192-cbc','aes256-cbc','3des-cbc','arcfour128','arcfour256')
        paramiko.util.log_to_file("filename.log")
    	ssh = paramiko.SSHClient()
    	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    	ssh.connect(x, username="halt", password="halt")
    	#print "P-"+x
    except paramiko.AuthenticationException:
    	print "F-"+x
    	'''
    	try:
    	 	paramiko.Transport._preferred_ciphers = ('diffie-hellman-group1-sha1')
			sshclient = paramiko.SSHClient()
			sshclient.load_system_host_keys()
			sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			sshclient.connect(x, username="admin", password="password")
		except paramiko.AuthenticationException:
		  	print "Not Connected 2ndTry..--" + x
		  	pass
		finally:
		  	sshclient.close()   	
		'''
    except:
    	 pass
    finally:
       	ssh.close()   

if __name__ == "__main__":
    p = Pool(10)
    with open('ip.txt') as source_file:        	
        	results=p.map(process_line,source_file)
        	p.map(async_reqest,results,10)
    
    
