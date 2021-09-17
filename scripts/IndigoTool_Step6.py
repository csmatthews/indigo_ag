# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:17:17 2021

@author: cmatthews
"""
### Run these in a command line

pgsql2shp -f "facilities2020total.shp" -h localhost -u postgres -P  indigo public.facilities
