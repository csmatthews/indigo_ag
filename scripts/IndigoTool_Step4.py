# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:25:32 2021

@author: cmatthews
"""

#Run in QGIS

processing.run("native:joinattributesbylocation", 
{'INPUT': 'postgres://dbname=\'indigo\' host=localhost port=5432 user=\'postgres\' password=\'ccubed\' sslmode=disable key=\'gid\' srid=102005 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"facilities_buf25mi\" (geom)',
'JOIN': 'postgres://dbname=\'indigo\' host=localhost port=5432 user=\'postgres\' password=\'ccubed\' sslmode=disable key=\'gid\' srid=4326 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table=\"public\".\"counties\" (geom)',
'PREDICATE':[0],
'JOIN_FIELDS':['total2020value'],
'METHOD':0,
'DISCARD_NONMATCHING':False,
'PREFIX':'',
'OUTPUT': 'postgres://dbname=\'indigo\' host=localhost port=5432 user=\'postgres\' password=\'ccubed\' sslmode=disable table=\"public\".\"facilities_buf25mi_joincounties\" (geom)'})

### Run Step 5 "C:\Users\cmatthews\Desktop\Indigo\Tool\IndigoTool_Step3.py"
print("Move onto Run IndigoTool_Step5.py")