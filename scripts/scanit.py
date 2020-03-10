#!/usr/bin/env python3

import json
import request

API_KEY = '' # YOUR API KEY GOES HERE!!


# 88888888888888888888888888888888888888
''' 
purpose: send a GET request
         to VirusTotal to retrieve the 
         scan results.
param: the md5 hash of the
       file/s that will be scanned
'''
# 88888888888888888888888888888888888888
def get_results(md5_hash):
	url = 'https://www.virustotal.com/vtapi/v2/file/report'

	params = {'apikey': API_KEY, 'resource': md5_hash}

	resp = requests.get(url, params=params)

	return resp.json()
