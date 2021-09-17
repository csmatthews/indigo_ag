# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:14:54 2021

@author: cmatthews
"""

import psycopg2
conn = psycopg2.connect("host=localhost dbname=indigo user=postgres password=")


### Summarize Facility Totals to Single Ids

cur = conn.cursor()

cur.execute("""  
    select 
	gid,
	sum(Total2020Value) as total2020value 
    into facility_totals
    from facilities_buf25mi_joincounties
    group by gid
     """)
     
     
     
### Update Facilities SHP with Total Values

cur.execute("""  
    UPDATE facilities AS f 
    SET total2020value = ft.total2020value
    FROM facility_totals AS ft
    WHERE f.gid = ft.gid 
     """)
     
          
conn.commit()

print("Finished Summarize Facility Totals to Single Ids")
print("Update Facilities SHP with Total Values")

### Run Step 6 "C:\Users\cmatthews\Desktop\Indigo\Tool\IndigoTool_Step6.py"
print("Move onto Run IndigoTool_Step6.py")
