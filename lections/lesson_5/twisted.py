# TWISTED

class AccessorType(type):
    def __init__(self, name, bases, d):
        type.__init__(self, name, bases, d)
        accessors = {}
        prefixs = ["get_", "set_", "del_"]
        for k in d.keys():
            v = getattr(self, k)
            for i in range(3):
                if k.startswith(prefixs[i]):
                    accessors.setdefault(k[4:], [None, None, None])[i] = v
        for name, (getter, setter, deler) in accessors.items():
            # create default behaviours for the property - if we leave
            # the getter as None we won't be able to getattr, etc..

            # [...] some code that implements the above comment

            setattr(self, name, property(getter, setter, deler, ""))


class A(metaclass=AccessorType):
    def get_me(self):
        return 1


a=A()

print(a.me)