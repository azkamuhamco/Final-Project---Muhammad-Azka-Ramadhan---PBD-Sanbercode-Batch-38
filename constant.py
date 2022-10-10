from dotenv import dotenv_values
from sqlalchemy import create_engine
from mysql.connector import connect

params   = {"db": dotenv_values(".env")}
host     = params['db']['MYSQL_HOST']       
user     = params['db']['MYSQL_USERNAME']   
password = params['db']['MYSQL_PASSWORD']   
database = params['db']['MYSQL_DB']         
port     = params['db']['MYSQL_PORT']       
engine   = create_engine("mysql+pymysql://"+user+":"+password+"@"+host+"/"+database+"")

db       = connect(
            host     = params['db']['MYSQL_HOST']    , 
            user     = params['db']['MYSQL_USERNAME'], 
            password = params['db']['MYSQL_PASSWORD'], 
            database = params['db']['MYSQL_DB']      , 
            port     = params['db']['MYSQL_PORT']    
)