class Count:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.n = self.max
        return self
    def __next__(self):
        res = self.n
        self.n -= 1
        if(res < 0):
            raise StopIteration
        return res
a = Count(int(input()))
for i in a:
    print(i)