from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.log import Log
from app.workers.tasks import process_log
from app.schema.log import LogCreate
from app.services.decision_engine import decide_action
router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@router.post("/logs")
def create_log(log: LogCreate, db: Session = Depends(get_db)):
	
	

	new_log = Log(
		message=log.message,
		level=log.level,
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

@router.get("/logs/{log_id}")
def get_log(log_id: int, db: Session = Depends(get_db)):

	log=db.query(Log).filter(Log.id == log_id).first()

	if not log:
		return {"error":"Log not found"}

	return {
		"id":log.id,
		"message":log.message,
		"level":log.level,
		"status":log.status,
		"analysis":log.analysis,
	}
