# Import all needed libarys
import time
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.gpio import GPIO
import sys
import logging
from datetime import datetime
#from grove.factory import Factory
import psycopg2

# Database Connection
conn = psycopg2.connect(
    dbname="plantdb", 
    user="pi", 
    password="", 
    host="localhost", port ="5432")

conn.autocommit = True

# Connect to Moisture Sensor, connect to alalog pin 2(slot A2)
sensor_moist = GroveMoistureSensor(0)

# Connect to Temp Sensor
#sensor_temp = Factory.getTemper("NTC-ADC", 2)
sensor_temp = GroveMoistureSensor(2)

# Define Logging
logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG) 

def main():

    while True:
        # moist
        m = sensor_moist.moisture

        # Temp
        temp = sensor_temp.moisture
        #temp = 0
        
        # Motion Sensor
        Motion_value = GPIO(5, GPIO.IN)

        # Value for Logs
        now = datetime.now()

        logs = f" python_datetime: {now}, moisture_value: {m}, temp_value: {temp}, motion_value: {Motion_value.read()}"
        logging.debug(logs)
        print(logs)

        # # Database plant_times_series_data
        cursor = conn.cursor()
        statement = f""" 
        insert into people2 values(
            '{now}', 
            '{m}',
            '{temp}',
            '{Motion_value.read()}');

        """
        cursor.execute(statement)
        conn.commit()
        conn.close()

        # Sleep for 1 Second, we dont want to get to much data, i hope
        time.sleep(1)

if __name__ == '__main__':
    main()