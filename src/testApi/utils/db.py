import psycopg2
from Models.Devices import create_table_device
from Models.Endpoint import create_table_endpoint
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import db_server_host, db_username, db_server_port, db_password

connection = psycopg2.connect(user=db_username,
                              password=db_password,
                              host=db_server_host,
                              port=db_server_port)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()

def create_db():


    cursor.execute(create_table_device())
    cursor.execute(create_table_endpoint())
    connection.commit()

def add_device(dev_id, dev_type ):
    create_db()
    cursor.execute(f"INSERT INTO devices (dev_id, dev_type) VALUES( %s, %s);", (dev_id,dev_type))
    connection.commit()

def get_device(dev_id, dev_type):
    cursor.execute(f"SELECT * FROM devices WHERE dev_id=%s and dev_type=%s;", (dev_id,dev_type))
    connection.commit()
    return cursor.fetchall()

def add_endpoint(device_id, comment ):
    create_db()
    cursor.execute(f"INSERT INTO endpoints (device_id, comment) VALUES( %s, %s);", (device_id,comment))
    connection.commit()

def get_devices_without_endpoint1():
    cursor.execute(
        f'SELECT dev_type, COUNT(*) AS ModelsCount from devices as devices where devices.id NOT IN (SELECT endpoints.device_id from endpoints as endpoints ) GROUP BY dev_type;')
    return cursor.fetchall()
