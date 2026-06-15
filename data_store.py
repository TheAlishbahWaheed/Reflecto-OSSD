"""
data_store.py — file-based JSON storage (mirrors data.php)
"""
import os, json, re
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def _user_file(user: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_\-]", "_", user)
    return os.path.join(DATA_DIR, safe + ".json")

def load_user(user: str) -> dict:
    f = _user_file(user)
    if not os.path.exists(f):
        return {"journal":[],"notes":[],"tasks":[],"moods":[],"theme":"light"}
    try:
        with open(f, "r", encoding="utf-8") as fp:
            return json.load(fp)
    except:
        return {"journal":[],"notes":[],"tasks":[],"moods":[],"theme":"light"}

def save_user(user: str, data: dict) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(_user_file(user), "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)

def delete_user(user: str) -> bool:
    f = _user_file(user)
    if os.path.exists(f):
        os.remove(f)
        return True
    return False

def reset_user(user: str) -> None:
    theme = load_user(user).get("theme","light")
    save_user(user, {"journal":[],"notes":[],"tasks":[],"moods":[],"theme":theme,"lastLogin":datetime.now().isoformat()})

def list_users() -> list:
    if not os.path.isdir(DATA_DIR):
        return []
    users = []
    for f in os.listdir(DATA_DIR):
        if f.endswith(".json"):
            name = f[:-5]
            try:
                with open(os.path.join(DATA_DIR, f), "r", encoding="utf-8") as fp:
                    d = json.load(fp)
            except:
                d = {}
            users.append({"name": name, "lastLogin": d.get("lastLogin","")})
    users.sort(key=lambda u: u["lastLogin"], reverse=True)
    return users
