class Count:
    def __init__(self, b, a):
        self.a = a
        self.b = b

    def __iter__(self):
        self.n = self.b
        return self
    def __next__(self):
        k = self.n
        self.n += 1
        if(self.a < k):
            raise StopIteration
        return pow(k, 2)
a = int(input())
l = Count(a, int(input()))
for i in l:
    print(i)