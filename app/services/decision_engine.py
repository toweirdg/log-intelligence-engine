def decide_action(category, pattern):

	if category == "ERROR":
		return "Trigger alert"

	if pattern and "timout" in pattern:
		return "Check server load"

	return "No action needed"
