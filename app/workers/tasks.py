from app.workers.celery_app import celery_app

from app.services.log_processor import (
    categorize_log,
    detect_error_patterns,
    detect_repeated_patterns
)

from app.services.decision_engine import decide_action

from app.db.session import SessionLocal
from app.models.log import Log


@celery_app.task
def process_log(log_id: int, message: str):

    print(f"Processing log {log_id}: {message}")

    db = SessionLocal()

    try:
        category = categorize_log(message)
        pattern = detect_error_patterns(message)
        is_repeated = detect_repeated_patterns(message)

        action = decide_action(category, pattern)

        if "error" in message.lower():
            status = "processed_error"
        else:
            status = "processed"


        log_entry = db.query(Log).filter(Log.id == log_id).first()

        if log_entry:
            log_entry.level = category
            log_entry.status = status
            log_entry.pattern = str(pattern)
            log_entry.action = action

            db.commit()

            print(f"[UPDATED] Log {log_id} updated successfully")

        else:
            print(f"[ERROR] Log {log_id} not found")

    except Exception as e:
        print(f"[CELERY ERROR]: {e}")

    finally:
        db.close()
