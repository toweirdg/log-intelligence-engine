from app.workers.celery_app import celery_app

from app.services.log_processor import (
    categorize_log,
    detect_error_patterns
)


@celery_app.task
def process_log(log_id: int, message: str):
	print(f"Processing log {log_id}: {message}")

	category = categorize_log(message)
	pattern = detect_error_patterns(message)
        
	print(f"[Log {log_id}] Category: {category}")
	print(f"[Log {log_id}] Pattern: {pattern}")

     
	if "error" in message.lower():
		result="High severity issue detected"
	else:
		result="Normal log"

	print(f"Final Result:{result}")
	
	return {
        "log_id": log_id,
        "category": category,
        "pattern": pattern,
        "result": result
    }
