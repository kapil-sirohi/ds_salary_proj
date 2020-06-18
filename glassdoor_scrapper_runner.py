# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:11:51 2020

@author: kapil
"""


import glassdoor_scrapper as gs
import pandas as py

path = "C:\\Users\\kapil\\Downloads\\chromedriver_win32\\chromedriver.exe"

df = gs.get_jobs(5, False, path, 2)