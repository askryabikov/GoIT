d={ 'a':1,
    3:'b',
    2:4,
    'd':'e',
   (1,1):[7,8],
}
print (d)
# print(d.items())
print(d.keys())
print(d.values())
print(d.get(2))
# print(d.get(3, 'not found'))
print(d[2])
# print(d['a'])
# d['a']=100
# print(d)
# print(d['a'])
d['x']=10
print(d)
# d['c']=100
# print(d)

# for _ in d:
#     print(_)
d1={}
for i in range(100):
    d1[i]=i*i
print(d1)
