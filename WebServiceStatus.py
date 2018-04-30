#!/usr/bin/env python

import subprocess
import os
import sys 
import json
import urllib

webUrl = "http://localhost:8983/solr/admin/info/system?wt=json"
solrJSONResonse = urllib.urlopen(webUrl)
solrJSONData=json.loads(solrJSONResonse.read())
totalPhysicalMemorySize=solrJSONData["system"]["totalPhysicalMemorySize"]
freePhysicalMemorySize=solrJSONData["system"]["freePhysicalMemorySize"]
solrMemory = (totalPhysicalMemorySize-freePhysicalMemorySize)*100/totalPhysicalMemorySize
print solrMemory
