from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import OperationalError
import asyncio
import sys

sys.path.append('../..')

username = 'shaya'
password = '12235Tal'
host = 'llm.mysql.database.azure.com'
database = 'LLM_Evaluator'

# Define the database connection
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:3306/{database}')
meta = MetaData()

try:
    # Attempt to connect to the database
    con = engine.connect()
    print("Connection to the database successful.")
except OperationalError as e:
    print("Error connecting to the database:", e)
