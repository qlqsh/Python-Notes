#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

# HTTP认证
auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)