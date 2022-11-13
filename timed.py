import time 
def timeme(func):
    def wrapper(): 
        start = time.time() 
        func()
        end = time.time() 
        mytime = end-start
        print
        print(f"Total time, {end - start}") 
    return wrapper
