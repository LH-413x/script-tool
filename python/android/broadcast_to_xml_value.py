#!/usr/bin/python
# -*- coding: UTF-8 -*-

head='''
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="filterd_broadcast_names">
'''

print head

with open("/home/alex/android-note/broadcast/broadcast_can_be_send_to_bluetooth") as f:
    for line in f:
        print "        <item>{}</item>".format(line.replace('\n',''))

rear='''
    </string-array>

</resources>
'''

print rear
