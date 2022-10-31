import collections

class FifoQueue(collections.deque):
    def __init__(self):
        super().__init__()

    def isEmpty(self):
        return len(self) == 0

    def isFull(self):
        return len(self) == self.maxlen

    def size(self):
        return len(self)

    def front(self):
        return self[0]

    def rear(self):
        return self[-1]

    def enque(self, elem):
        self.append(elem)

    def deque(self):
        return self.popleft()

def main():
    fq = FifoQueue()

    print(fq.isEmpty())
    print(fq.isFull())
    fq.enque(1)
    fq.enque(2)
    fq.enque(3)
    print(fq.front())
    print(fq.rear())
    print(fq.size())
    print(fq.isEmpty())
    print(fq.deque())
    print(fq.front())
    print(fq.deque())
    print(fq.deque())
    print(fq.isEmpty())

if __name__ == "__main__":
    main()