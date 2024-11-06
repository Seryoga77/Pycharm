class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


import inspect


def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
    info['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info['methods'] = methods

    info['module'] = obj.__module__

    info['doc'] = inspect.getdoc(obj)

    return info


my_object = MyClass("Alice")
object_info = introspection_info(my_object)
print(object_info)
