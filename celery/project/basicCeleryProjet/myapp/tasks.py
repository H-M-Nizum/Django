from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(25)
    return f"The Addition of {x} and {y} is : {x + y}"

@shared_task
def sub(x, y):
    time.sleep(20)
    return f"Then Subtraction of {x} and {y} is : {x - y}"

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Clear for : {id}")
    return id


@shared_task
def clear_redis_data(key):
    print(f"Redis Data Clear for : {key}")
    return key