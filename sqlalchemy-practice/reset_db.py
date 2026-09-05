"""Reset practice database — drops and recreates all tables from models.py."""
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from models import Base

load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)

confirm = input(f"This will DROP ALL TABLES in database '{db_name}'. Type 'yes' to continue: ")
if confirm == "yes":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Tables dropped and recreated.")
else:
    print("Aborted.")