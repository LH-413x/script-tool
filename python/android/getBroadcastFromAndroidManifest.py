#!/usr/bin/python
import re

s=''
with open("AndroidManifest.xml") as f:
    s = f.read()
pattern = re.compile(r'(<action\s+android:name\s*=\s*")(\S+)("\s*/>)')
result = pattern.findall(s)

if not result:
    print "No search"

for i in result:
    print "<item>{}</item>".format(i[1])
