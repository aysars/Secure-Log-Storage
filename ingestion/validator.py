def validate_log(log):
    if not isinstance(log, str):
        raise ValueError("Log must be a string")
    if log.strip() == "":
        raise ValueError("Log cannot be empty")
    return log
