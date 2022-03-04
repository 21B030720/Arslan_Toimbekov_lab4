import datetime
a = datetime.datetime.now()
for i in range(5):
    print(a)
    a = a + datetime.timedelta(days=1)