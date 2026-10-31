import os
from urllib.parse import urlparse
from dotenv import load_dotenv
def get_mysql_config():

    load_dotenv()

    jdbc_url = os.getenv('MYSQL_URL')

    parse_jdbc = urlparse(jdbc_url.replace('jdbc:','', 1))
    host = parse_jdbc.hostname
    port = parse_jdbc.port
    database = parse_jdbc.path.replace('/','')
    password = os.getenv('MYSQL_PASSWORD')
    user = os.getenv('MYSQL_USER')

    return {
        'host': host,
        'port': port,
        'user': user,
        'password': password,
        'database': database
    }