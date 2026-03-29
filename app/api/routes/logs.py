from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.log import Log
from app.workers.tasks import process_log

router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@router.post("/logs")
def create_log(log: dict, db: Session = Depends(get_db)):

	new_log = Log(
		message=log.get("message"),
		level=log.get("level","INFO"),
		status="pending" 	
	)
	
	db.add(new_log)
	db.commit()
	db.refresh(new_log)

	process_log.delay(new_log.id, new_log.message)


	return{
		"id":new_log.id,
		"message":new_log.message,
		"status":"queued for processing"
	}
