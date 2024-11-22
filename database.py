from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(mysql+pymysql://jayparikh:Fyndtest@123@jayparikh.mysql.pythonanywhere-services.com/jayparikh$fynd)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()