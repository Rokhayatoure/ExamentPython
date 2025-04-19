# config/redis_client.py
import redis
from config.settings import REDIS_HOST, REDIS_PORT, REDIS_DB

# Connexion simple (sans mot de passe)
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True  # pour avoir des strings au lieu de bytes
)

# Connexion avec mot de passe (si besoin)
# redis_client = redis.Redis(
#     host=REDIS_HOST,
#     port=REDIS_PORT,
#     db=REDIS_DB,
#     password=REDIS_PASSWORD,
#     decode_responses=True
# )
