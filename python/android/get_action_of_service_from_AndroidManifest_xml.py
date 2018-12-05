#!/usr/bin/python
# -*- coding: UTF-8 -*

from xml.dom.minidom import parse
import xml.dom.minidom
from termcolor import *


DOMTree = xml.dom.minidom.parse("AndroidManifest.xml")
collection = DOMTree.documentElement

services= collection.getElementsByTagName("service")

enabled_list=[]
condition_enabled_list=[]

for service in services:
    if not service.getElementsByTagName('intent-filter'):
        continue
    intent_filter = service.getElementsByTagName('intent-filter')[0]
    action = intent_filter.getElementsByTagName('action')[0]
    action_name = action.getAttribute('android:name')   
    service_name = service.getAttribute('android:name')
    if service.hasAttribute("android:enabled"):
        enabled = service.getAttribute('android:enabled')
        if enabled == 'false':
            continue
        if enabled != 'true':
            condition_enabled_list.append([service_name,action_name,enabled]) 
    
    enabled_list.append([service_name,action_name])

print 'enabled == true:'
for i in enabled_list:
    print '{} {}'.format(colored(i[0],'blue'),colored(i[1],'green'))

print ''
print 'condition enabled:'
for i in condition_enabled_list:
    print '{} {} {}'.format(colored(i[0],'blue'),colored(i[1],'green'),colored(i[2],'yellow'))
