class Count:
    def __init__(self, a):
        self.a = a

    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        k = self.n
        self.n += 1
        if(self.a < k):
            raise StopIteration
        return pow(k, 2)
a = int(input())
l = Count(a)
for i in l:
    print(i)