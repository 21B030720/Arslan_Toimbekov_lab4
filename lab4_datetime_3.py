import datetime
a = datetime.datetime.now()
a = str(a)
m = a.rindex(".")
#print(m)
a = a[:m]
print(a)