from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import OperationalError
import asyncio
import sys

sys.path.append('../..')

# Define the database connection
engine = create_engine('mysql+pymysql://root:12235tal@localhost:3306/LLM_Evaluator')
meta = MetaData()

try:
    # Attempt to connect to the database
    con = engine.connect()
    print("Connection to the database successful.")
except OperationalError as e:
    print("Error connecting to the database:", e)
