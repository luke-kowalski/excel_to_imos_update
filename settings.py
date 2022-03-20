from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.ini")

SQL_driver = parser.get("SERVER_CONN", "SQL_DRIVER")
SQL_server = parser.get("SERVER_CONN", "SQL_SERVER")
SQL_database = parser.get("SERVER_CONN", "SQL_DATABASE")
SQL_username = parser.get("SERVER_CONN", "SQL_USERNAME")
SQL_password = parser.get("SERVER_CONN", "SQL_PASSWORD")
