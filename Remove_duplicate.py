def remove_duplicate(number):
	
	lst = []
	
	for i in number:
		if i not in lst:
			lst.append(i)
	print (lst)
	
remove_duplicate([1,1,1,2,2,3,4])
