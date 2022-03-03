class Count:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.n = 2
        return self
    def __next__(self):
        res = self.n
        self.n += 2
        if(res > self.max):
            raise StopIteration
        return res
a = Count(int(input()))
for i in a:
    print(i)