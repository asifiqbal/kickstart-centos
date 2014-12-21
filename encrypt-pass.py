#!/usr/bin/python
import sys, crypt 

if len(sys.argv) != 2:
    print "Usage: %s <password>" % str(sys.argv[0])
    exit(1)

mypass = sys.argv[1]

mysalt = "$6$2p6bRbo5" # sha512 

secret = crypt.crypt(mypass, mysalt)

print secret
