import json
from models import Profile

def load_profiles(json_path="profiles.json"):
    with open(json_path, "r") as f:
        raw_data = json.load(f)
    
    profiles = [Profile(**item) for item in raw_data]
    return profiles
