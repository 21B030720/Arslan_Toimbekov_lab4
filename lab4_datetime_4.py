import datetime
a = datetime.datetime.now()
b = a + datetime.timedelta(days = int(input()))
#b = b.strftime(2000, 8, 7)
c = b - a
print(c.days*24*3600)
