def sum(a,b):
        '''
        Sums two integers up without using math operators like + and -
        '''
	r = a^b
	c = (a&b)<<1
	if c:
		return sum(r,c)
	return r


assert sum(1,2) == 3
assert sum(100,333) == 433
assert sum(254,1) == 255
assert sum(1234,1234) == 2468 
