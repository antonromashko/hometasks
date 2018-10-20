models = {}


class ModelMetaclass(type):
    def __new__(meta, name, bases, attrs):
        models[name] = cls = type.__new__(meta, name, bases, attrs)
        return cls


print(models)


class Model(metaclass=ModelMetaclass):
    pass


print(models)


class MyModel(Model):
    pass


print(models)