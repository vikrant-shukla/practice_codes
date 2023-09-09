# s = 'xyziczfx'
# new = s.replace('y',"").replace("f","")
# print(new)

# if new == new[::-1]:
#     print("its palindrome")
# else:
#     print("its not")



"""Decorators"""
# def element(func):
#     def wrapper():
#         data1 = {"num1" : 5,"num2":5}
#         return func(**data1)
#     return wrapper


# @element
# def test(**kwargs):
#     return kwargs.get("num1") + kwargs.get("num2")
# print(test())

import time


def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        difference = end - start
        print({f"time_took by {func.__name__}": difference})
    return wrapper

@execution_time
def func_range():
    for i in range(50):
        print(i)
func_range()