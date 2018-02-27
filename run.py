#!/usr/bin/env python

from amodule.ansibleapi import ansible_playbook
from optparse import OptionParser

parser = OptionParser(usage="usage: %prog [options] -f arg1 -p arg2")
parser.add_option("-f","--playbook-to-path",
                  action="store",type="string",dest="filename")
parser.add_option("-p","--password",
                  action="store",type="string",dest="password")


(opts, args)= parser.parse_args()
if (opts.filename==None or opts.password==None) and args==[]:
    print "see <script.py> -h  for more info....."
else:
    ansible_playbook(pbpath=opts.filename,password=opts.password)


