from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.log import Log

router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@router.post("/logs")
def create_log(log: dict, db: Session = Depends(get_db)):
	print("Incoming log:", log)

	new_log = Log(
		message=log.get("message"),
		level=log.get("level","INFO")
		)
	
	db.add(new_log)
	db.commit()
	db.refresh(new_log)

	print("Saved log ID:", new_log.id)

	return{
		"id":new_log.id,
		"message":new_log.message,
		"status":"stored"
	}
