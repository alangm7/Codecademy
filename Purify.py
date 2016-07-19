'''crea una funcion que quite los impares de una lista'''


def purify(numbers):
	new = []
	for i in numbers:
		if i % 2 == 0:
			new.append(i)
	print (new)
	
purify([1,2,1,2,3,3,4,54,5,3])
