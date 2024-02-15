#Saud AlQahtani
# 442101254

# Program with a decorator to repeat the call of hello() function a certain number of times.

def repeat_hello(func):
    def wrapper():
        x = int(input("Enter a number of repetitions: "))
        for _ in range(x):
            func()
    return wrapper

@repeat_hello
def hello():
    print('Hello')

hello()
