import threading

def locked_method(func):
    def new_method(self, *args, **kwargs):
        with self.lock:
            func(self, *args, **kwargs)

    return new_method

class DecoratorList(list):
    def __init__(self, *args, **kwargs):
        self.lock = threading.Lock()
        super(DecoratorList, self).__init__(*args, **kwargs)

    @locked_method
    def insert(self, idx, obj):
        super(DecoratorList, self).insert(idx, obj)

    @locked_method
    def remove(self, obj):
        super(DecoratorList, self).remove(obj)

def main():
    decoratorList = DecoratorList()
    decoratorList.insert(0, 'first')
    decoratorList.insert(0, 'second')
    decoratorList.insert(0, 'third')

    decoratorList.remove('second')

    print(decoratorList)

if __name__ == "__main__":
    main()