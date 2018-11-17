import inspect

cls_name = input("Class name: ")

args = {}


def data():
    arg = input("Enter param: ")
    while arg:
        yield arg
        arg = input("Enter param: ")


for i in data():
    try:
        name, value = i.split('=')

        if not name.isidentifier():
            raise NameError

        args[name] = eval(value)

    except (ValueError, NameError):
        print("Something went wrong. Please retry.")


def mystr(self):
    members = [f"\t{k}={v}\n" for k, v in inspect.getmembers(self)
                               if not any([inspect.ismethod(k), k.startswith('__'), k.endswith('__')])]

    return "Class <{}>\n{}".format(self.__class__.__name__, ''.join(members))


new_type = type(cls_name, (), args)
new_type.__str__ = mystr

obj = new_type()

print(obj)
