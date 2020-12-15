# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önce işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#         return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)

# sayHello("ahmet")

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):

        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+func.__name__+ " " + str(finish-start)+ " saniye sürdü.")
    return inner

@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usAlma(2,3)
faktoriyel(4)
toplama(10,20)