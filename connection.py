import pyodbc
from configparser import ConfigParser

cf=ConfigParser()
cf.read("Config.ini")
Driver=cf.get("data","driver")
Host=cf.get("data","host")
user=cf.get("data","user")
password=cf.get("data","password")
database=cf.get("data","database")

class Connection:
    def __init__(self) -> None:
        self.conn=pyodbc.connect(driver=Driver,host=Host,user=user,password=password,database=database)
        self.cursor=self.conn.cursor()
        