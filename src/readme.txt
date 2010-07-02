>>> import time
>>> from redispool import RedisPool

>>> for i in xrange(10000):
...     pool = RedisPool()
...     conn = pool.connection()
...     conn.set('test','world')
...     conn.get('test')
...     pool.close(conn)
True
...