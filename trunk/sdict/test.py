import sdict
d = sdict.Dict()
d['123']='haha value'
print d['123']

d['a/b/c']='xxxxx'
d['a/b/zz']='yyyy'
d['a/zz']='zzzzz'
print d.prefix('a/')
print d.keys()
print d.values()
print 'len:',len(d)
print d

x = sdict.Dict()
for i in xrange(100):
    x[i] = i+1
del x[33]

print x.greater(33)
print 'len:',len(x)

