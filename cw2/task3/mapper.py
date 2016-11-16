#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import xml.etree.ElementTree as ET
for line in sys.stdin:
    line = line.strip()
    root = ET.fromstring(line)
    if root.attrib['PostTypeId'] == '2':
        print("{0}\t{1}\t{2}".format(root.attrib['OwnerUserId'], 1, root.attrib['ParentId']))
