from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


host = os.getenv("DB_HOST"),
database = os.getenv("DB_NAME"),
user = os.getenv("DB_USER"), 
password = os.getenv("DB_PASSWORD"),
port = os.getenv("DB_PORT"),

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@counsellingdb:{port}/{database}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
