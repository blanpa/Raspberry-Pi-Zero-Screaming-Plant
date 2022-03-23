import psycopg2

# from sqlalchemy import create_engine
print(sysconfig.get_platform())

try:
    if sysconfig.get_platform() == "linux-armv7l":
        path = os.path.join("/home", "pi", "Code", "Confidental", "psswd.txt")
        PASSWORD = open(path, mode = "r").read()
    else:
        PASSWORD = open(os.path.join("..", "Confidental", "passwd.txt"), mode = "r").read()

    print("Got the right Password")
except:
    print(path)
    print("Password is not in the Confidental Directory!")
    exit()


conn = psycopg2.connect(
    dbname="plantdb", 
    user="pi", 
    password=PASSWORD, 
    host="localhost", port ="5432")

conn.autocommit = True

cursor = conn.cursor()

statement = """ 
CREATE TABLE testtest1 (
	ts timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
	moisture_value int4 NULL,
	temp_value int4 NULL,
	motion_value int4 NULL);
"""
#SELECT create_hypertable('tbl_xyz', 'ts');

# plant_times_series_data
#	uuid uuid NULL,

cursor.execute(statement)
  
conn.commit()
conn.close()