from typing import List
from sqlalchemy import ForeignKey
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)

class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ = "patients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

    appointments: Mapped[List["Appointment"]] = relationship(back_populates="patient")

class Appointment(Base):
    __tablename__ = "appointments"
    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    date: Mapped[str]
    reason: Mapped[str]

    patient: Mapped["Patient"] = relationship(back_populates="appointments")

Base.metadata.drop_all(engine)   # drops patients + appointments (FK-aware order)
Base.metadata.create_all(engine)