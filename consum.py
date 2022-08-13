import time
import redis
from tasks import pool

def con():
    r = redis.Redis(connection_pool=pool,db=3)
    last_id = 0
    total = r.xlen("mydb")
    print(type(total))
    while 1:
        if not last_id:
            ret = r.xrange("mydb", "-", "+", count=2)
            
        else:
            ret = r.xrange("mydb", f"{last_id}", "+", count=2)

        if ret:
            last_id_str = ret[-1][0]
            last_id_main, last_id_index = last_id_str.split("-")
            last_id = f"{last_id_main}-{int(last_id_index)+1}"
        print(f"get:{ret}")
        if len(ret) < 2:
            time.sleep(20)
        time.sleep(5)
        
        
if __name__ == '__main__':
    con()