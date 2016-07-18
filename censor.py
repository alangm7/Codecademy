def censor(text, word):
	
	lst = text.split()
	for i in lst:
		if word in lst:
			loc = lst.index(word)
			lst.remove(word)
			lst.insert(loc, "*" * len(word))
			newLst = " ".join(lst)
			
	print (newLst)
		
censor('esto es un hack', 'hack')
