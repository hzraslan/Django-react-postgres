import time
import random
START_TIME = 1464972048475.8179

def create_id():
    t = int(int(time.time()*1000) - START_TIME)
    u = random.SystemRandom().getrandbits(23)
    id = (t << 23 ) | u
    return str(id)

def reverse_id(id):
    t  = id >> 23
    return t + START_TIME