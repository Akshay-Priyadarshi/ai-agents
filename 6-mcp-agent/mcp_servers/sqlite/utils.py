from pathlib import Path

def get_relative_path(path: str = None) -> str:
    return str((Path(__file__).parent)) if path is None else f"{str((Path(__file__).parent))}{path}"

def get_db_path():
    return get_relative_path("/database.db")

def get_log_path():
    return get_relative_path("/activity.log")

def get_script_path():
    return get_relative_path("/server.py")