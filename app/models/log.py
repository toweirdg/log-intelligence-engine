from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base

class Log(Base):
	__tablename__="logs"

	id = Column(Integer, primary_key=True, index=True)
	message = Column(String, nullable=False)
	level = Column(String, default="INFO")
	timestamp = Column(DateTime, default=datetime.utcnow)
	status = Column(String, default="pending")
