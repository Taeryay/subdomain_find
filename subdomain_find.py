# This is a sample Python script.
# This script is used to discover subdomains.
from itertools import product
import subprocess

domain = 'baidu.com'
file = open("test.txt","w")

for re in range(2,4):
    seq = product('abcdefghijklmnopqrstuvwxyz', repeat=re)
    for i in seq:
        s = ''.join(i)
        subdomain = s + '.' + domain
        ret = subprocess.call("ping -c 1 %s " % subdomain, shell=True)
        if ret == 0:
            print(subdomain, "+++++++++++++Online ")
            file.write(subdomain + "\n")
        else:
            print(subdomain, "-------------Offline")
file.close()