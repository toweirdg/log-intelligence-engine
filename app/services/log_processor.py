import re
from collections import Counter

def categorize_log(message: str):
	message = message.lower()

	if "error" in message:
		return "ERROR"
	elif "warning" in message:
		return "WARNING"
	else:
		return "INFO"

def detect_repeated_patterns(logs):
	return Counter(logs)

def detect_error_patterns(message: str):
	patterns =[
		r"timeout",
		r"connection refused",
		r"failed",
		r"execption"
	]

	for pattern in patterns:
		if re.search(pattern, message.lower()):
			return pattern
	
	return None
