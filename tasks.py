import time
from celery_app import app
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)

@app.task
def prod(name):
    r = redis.Redis(connection_pool=pool,db=3)
    print(f"==========={name}==========")
    time.sleep(5)
    ret = r.xadd("mydb", {"id": name})
    print(f"ret:{ret}")
    