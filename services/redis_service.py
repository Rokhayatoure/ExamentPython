import redis
import json
from config.settings import REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def cache_etudiant(etudiant_dict):
    key = f"etudiant:{etudiant_dict['telephone']}"
    r.set(key, json.dumps(etudiant_dict))

def get_cached_etudiant(telephone):
    key = f"etudiant:{telephone}"
    data = r.get(key)
    return json.loads(data) if data else None
