class MeCallable:

    def __call__(self, *args, **kwargs):
        for arg in args:
            yield arg

        for arg, value in kwargs.items():
            yield arg, value


obj = MeCallable()

for param in obj(1, 2, 3, data=4, x = 5):
    print(param)

print((MeCallable()(100, 200)))