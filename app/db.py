import os
from curses import meta
from databases import Database 

from sqlalchemy import (create_engine, MetaData, Column, String, DateTime,func, Table, Integer )
from sqlalchemy.sql import func

# database_url = "postgresql://mocha:Nyangau92@localhost:5432/fastapiDB"
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("email", String(50)),
    Column("id_number", Integer),
    Column("year", Integer),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fullname", String(50)),
    Column("email", String(50)),
    Column("password", String(250)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)
database = Database(database_url)