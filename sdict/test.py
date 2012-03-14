import sdict
d = sdict.Dict()
d['123']='haha value'
print d['123']

d['a/b/c']='xxxxx'
d['a/b/zz']='yyyy'
d['a/zz']='zzzzz'
print 'prefix a:',d.prefix('a/')
print 'all keys:',d.keys()
print 'all values:',d.values()
print 'length:',len(d)
print 'd =',d

x = sdict.Dict()
for i in xrange(100):
    x[i] = i+1
del x[33]

print 'keys greater or equal to 33', x.greater(33)
print 'keys less than or equal to 32,at most 5 listed',x.less(32,limit=5)

print 'length:',len(x)

