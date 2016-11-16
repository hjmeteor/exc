#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import xml.etree.ElementTree as ET
for line in sys.stdin:
    line = line.strip()
    root = ET.fromstring(line)
    if root.attrib['PostTypeId'] == '2':
        print("{0}\t{1}\t{2}".format(root.attrib['Id'], root.attrib['PostTypeId'], root.attrib['OwnerUserId']))
    else:
        if root.attrib.has_key('AcceptedAnswerId'):
            print("{0}\t{1}".format(root.attrib['AcceptedAnswerId'], root.attrib['PostTypeId']))


