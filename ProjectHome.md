sdict is a module implementing python's build-in dict interface, and it supports range search and prefix matching. sdict it is an extension written in c.

## Setup ##
  1. svn checkout http://sdict.googlecode.com/svn/trunk/ sdict
  1. cd sdict
  1. python setup.py install

> (if you want to use sdict in the current directory, please use 'python setup.py build\_ext --inplace' in the third step)

  * For windows users, please download the pre-compiled zip file from http://code.google.com/p/sdict/downloads/list, and unpack it to python's site-packages directory, or anywhere you like.

## Usage Example ##

```
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


```