class Count:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.n = 12
        return self
    def __next__(self):
        res = self.n
        self.n += 1
        if(res > self.max):
            raise StopIteration
        if(res % 3 == 0 and res % 4 == 0):
            return res
        else:
            return 0
a = Count(int(input()))
for i in a:
    if(i != 0):
        print(i)