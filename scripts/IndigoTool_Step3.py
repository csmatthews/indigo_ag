# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 08:12:36 2021

@author: cmatthews
"""

import psycopg2
import sys

conn = psycopg2.connect("host=localhost dbname=indigo user=postgres password=ccubed")



### Update and Create Tables
cur = conn.cursor()
cur.execute("""
    CREATE TABLE corngrain2020(
    id integer PRIMARY KEY,
    geoid text,
    corngrain2020value int)
    """)
    
cur.execute("""
    CREATE TABLE soybean2020(
    id integer PRIMARY KEY,
    geoid text,
    soybean2020value int)
    """)
    
cur.execute("""
    ALTER TABLE counties
    ADD corngrain2020value int,
    ADD soybean2020value int,
    ADD total2020value int   
    """)
    
cur.execute("""
    ALTER TABLE facilities
    ADD COLUMN total2020value int;
    """)


conn.commit()


### Upload CSV to Target Table (Credit - MyDataHack.com)
# Function
def pg_load_table(file_path, table_name, dbname, host, port, user, pwd):
    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port,\
         user=user, password=pwd)
        cur = conn.cursor()
        f = open(file_path, "r")
        cur.execute("Truncate {} Cascade;".format(table_name))
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
        cur.execute("commit;")
        conn.close()

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

# Import CSVs
file_path = 'CornGrain_2020_DF.csv'
table_name = 'corngrain2020'
dbname = 'indigo'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = 'ccubed'
pg_load_table(file_path, table_name, dbname, host, port, user, pwd)
file_path = 'Soybean_2020_DF.csv'
table_name = 'soybean2020'
pg_load_table(file_path, table_name, dbname, host, port, user, pwd)
print("Imported CSVs to Database")



### Update Tables
cur = conn.cursor()
  
cur.execute("""  
    UPDATE counties AS v 
    SET corngrain2020value = s.corngrain2020value
    FROM corngrain2020 AS s
    WHERE v.geoid = s.geoid 
     """)
     
cur.execute("""  
    UPDATE counties
    SET corngrain2020value = 0
    WHERE corngrain2020value IS NULL
     """)
     
cur.execute("""  
    UPDATE counties AS v 
    SET soybean2020value = s.soybean2020value
    FROM soybean2020 AS s
    WHERE v.geoid = s.geoid 
     """)
     
cur.execute("""  
    UPDATE counties
    SET soybean2020value = 0
    WHERE soybean2020value IS NULL
     """)
     
     
cur.execute("""  
    UPDATE counties
    SET total2020value = corngrain2020value + soybean2020value
     """)

conn.commit()
print("Updated Tables")

### Run Step 4 "C:\Users\cmatthews\Desktop\Indigo\Tool\IndigoTool_Step4.py"
print("Move onto Run IndigoTool_Step4.py")