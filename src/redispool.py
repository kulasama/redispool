import threading
import redis
import collections
import thread

lock = thread.allocate_lock()


class RedisPool(object):
    
    is_running = False
    pool_size = 80
    
    def __init__(self):
        cls = RedisPool
        if not cls.is_running:
            cls.pool = collections.deque()
            for i in xrange(cls.pool_size):
                conn = redis.Redis(host='127.0.0.1',port=6379,db=0)
                cls.pool.append(conn)
            cls.is_running = True
        
    
    def connection(self):
        lock.acquire()
        try:
            cls = RedisPool
            conn = cls.pool.pop()
            if conn is None:
                raise('out of pool')
            return conn
        except:
            import traceback
            traceback.print_exc()
        finally:
            lock.release()
            
        
    def close(self,conn):
        lock.acquire()
        try:
            cls = RedisPool
            cls.pool.append(conn)
        except:
            import traceback
            traceback.print_exc()
        finally:
            lock.release()
            
    def status(self):
        cls = RedisPool
        print 'pool size',len(cls.pool)
        print cls.is_running
    
    