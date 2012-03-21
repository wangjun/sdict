import sdict

index = sdict.Dict()
R = []

for line in open("endict.txt","rb"):
	#print line
	tup = line.rstrip().split('\t')
	en_word = tup[0]
	chn_word = tup[1:]
	chn_word = ' '.join(chn_word).decode('utf-8')
	R.append(chn_word)
	index[en_word] = chn_word 

while True:	
	word = raw_input(">> ")

	rel_words = index.prefix(word)

	for w in rel_words:
		print w,index[w]



