def format_text(text):
    """Format the input text by stripping whitespace and ensuring proper casing."""
    return text.strip().capitalize()

def validate_input(input_data):
    """Validate the input data to ensure it meets the required criteria."""
    if not input_data or not isinstance(input_data, str):
        raise ValueError("Input must be a non-empty string.")
    return True

def log_event(event):
    """Log events for debugging or tracking purposes."""
    with open("event_log.txt", "a") as log_file:
        log_file.write(f"{event}\n")