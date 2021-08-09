# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:25:16 2021

@author: cmatthews
"""
### Run these in a command line

shp2pgsql -s 4326 "tl_2020_us_county" counties | psql -h localhost -p 5432 -U postgres -d indigo
shp2pgsql -s 102005 "facilities_buf25mi.shp" facilities_buf25mi | psql -h localhost -p 5432 -U postgres -d indigo
shp2pgsql -s 102005 "facilities.shp" facilities | psql -h localhost -p 5432 -U postgres -d indigo

### Run Step 3 "C:\Users\cmatthews\Desktop\Indigo\Tool\IndigoTool_Step3.py"
print("Move onto Run IndigoTool_Step3.py")