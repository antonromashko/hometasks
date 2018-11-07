

class Tracker:

    def __init__(self):
        print("Tracker is created")

    def __call__(self, fn):
        def wrapper():
            print(f"Function {fn.__name__} is called")
            return fn()

        return wrapper


@Tracker()
def foo():
    print("Foo is called")



foo()
foo()