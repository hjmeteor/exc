#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import xml.etree.ElementTree as ET
for line in sys.stdin:
    line = line.strip()
    root = ET.fromstring(line)
    print(1)

    for Id in root.iter('ParentId'):
        print (Id.attrib)
