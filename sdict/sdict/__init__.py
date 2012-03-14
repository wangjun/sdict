import tst
INT_MAX = (1<<31 - 1)

class Dict(object):
	def __init__(self):
		self.__tst__ = tst.create_tst_db()

	def __del__(self):
		#print 'over'
		tst.free_tst_db(self.__tst__)

	def put(self,key,value):
		if isinstance(key,str):
			tst.tst_put(self.__tst__,key,value)
		elif isinstance(key,int) and key<(1<<32):
			tst.tst_put(self.__tst__,str(key).zfill(10),value)
		else:
			print 'invalid key'

	def get(self,key):
		if isinstance(key,str):
			return tst.tst_get(self.__tst__,key)
		elif isinstance(key,int) and key<(1<<32):
			return tst.tst_get(self.__tst__,str(key).zfill(10))
		else:
			print 'invalid key'

	def delete(self,key):
		if isinstance(key,str):
			tst.tst_delete(self.__tst__,key)
		elif isinstance(key,int) and key<(1<<32):
			tst.tst_delete(self.__tst__,str(key).zfill(10))
		else:
			print 'invalid key'

	def prefix(self,key,limit=INT_MAX,is_asc=1):
		result = []
		if isinstance(key,str):
			tst.tst_prefix(self.__tst__,key,result,limit,is_asc)
		else:
			print 'invalid key'
		return result

	def greater(self,key,limit=INT_MAX):
		result =[]
		int_flag = 0
		if isinstance(key,str):
			tst.tst_greater(self.__tst__,key,result,limit)
		elif isinstance(key,int) and key<(1<<32):
			int_flag = 1
			tst.tst_greater(self.__tst__,str(key).zfill(10),result,limit)
		else:
			print 'invalid key'
		if int_flag == 1:
			result = [int(x) for x in result]
		return result
	
	def less(self,key,limit=INT_MAX):
		result =[]
		int_flag = 0
		if isinstance(key,str):
			tst.tst_less(self.__tst__,key,result,limit)
		elif isinstance(key,int) and key<(1<<32):
			int_flag =1 
			tst.tst_less(self.__tst__,str(key).zfill(10),result,limit)
		else:
			print 'invalid key'

		if int_flag == 1:
			result = [int(x) for x in result]

		return result
		
	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,value):
		self.put(key,value)


	def __contains__(self,key):
		return self.get(key)!=None

	def __delitem__(self,key):
		self.delete(key)


	def keys(self):
		return self.greater(chr(0))

	def values(self):
		keys = self.keys()
		return [self.get(x) for x in keys]

		
