import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def get_path_processed(file_name) -> Path:
    return ROOT / "data" / "processed" / file_name

def get_path_raw(file_name: str):
    return  ROOT / "data" / "raw" / file_name