from fastapi import APIRouter

router = APIRouter()

@router.post("/logs")
def create_logs(log:dict):
	return{
		"status": "received",
		"log": log
	}
