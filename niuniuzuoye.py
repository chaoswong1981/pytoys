from random import *

def gen():
	a = randint(0,10)
	b = randint(0,a)
	#print '%d - %d = %d' %(a,b,a-b)
	return (a,b,a-b)

def gens():
	result = []
        flag = False
	while len(result) <= 30:
		res = gen()
		if res in result:
			continue
                if res[2] == 0:
                        if not flag:
                                flag = True
                        else:
                                continue
		result.append(res)

	return result

result = gens()
for res in result:
	print '%d - %d = %d' % res
