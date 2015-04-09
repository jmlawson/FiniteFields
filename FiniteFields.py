import math
def isprime(n):
	if n<2:
		return False
	else:
		for i in range(2,int(math.sqrt(n))+1):
			if n%i==0:
				return False
        return True


class FiniteField:
        def __init__(self, size):
                if not isprime(size):
                        raise ValueError('The number %d is not prime' % size)
                self.size=size
        def get_size(self):
                return self.size
        def get_mult_inverse(self, element):
                if element%self.get_size() == 0:
                        raise ValueError('0 does not have a multiplicative inverse')
                mod_element=element%self.get_size()
                for i in range(1, self.get_size()):
                        if (mod_element*i-1)%self.get_size()==0:
                                return i
        def get_add_inverse(self, element):
                return (-1*element)%self.get_size()
        def add(self, elt1, elt2):
                return (elt1+elt2)%self.get_size()
        def mult(self, elt1, elt2):
                return (elt1*elt2)%self.get_size()
      
