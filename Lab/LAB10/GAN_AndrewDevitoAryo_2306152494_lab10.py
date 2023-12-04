'''
Nama    : Andrew Devito Aryo
NPM     : 2306152494
Kelas   : DDP1 - C
Asdos   : GAN
'''

# Pecahan.py
gcd = lambda a, b: a if b == 0 else gcd(b, a%b);    """ Calculate the greatest common divisor of two positive integers """
lcm = lambda a, b: a*b // gcd(a, b);                """ Calculate the lowest common multiple of two positive integers."""

class Pecahan(object):
    def __init__(self, numer, denom = 1):
        """ Pecahan with numerator numer and denominator denom.
        The denominator parameter defaults to 1"""
        if denom != 0:
            self.numer = numer  
            self.denom = denom
        else:
            raise(ZeroDivisionError)
        
    def __str__(self):
        """ String representation for printing"""
        if self.denom != 1:
            return str(self.numer) + '/' + str(self.denom)
        else:
            return str(self.numer)
            
    def __repr__(self):
        """ Used in interpreter's response """
        return f"Pecahan{self.numer, self.denom}"
    
    def __add__(self, param):
        """ Add two Pecahans. Allows int as a parameter"""
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            the_lcm = lcm(self.denom, param.denom)
            numerator_sum = (the_lcm * self.numer // self.denom) + \
                (the_lcm * param.numer // param.denom)
            return Pecahan(numerator_sum, the_lcm)
        else:
            print("Wrong Type")
            raise(TypeError)
        
    def __sub__(self, param):
        """ Subtract two Pecahans"""
        # subtraction is the same but with '-' instead of '+'
        if type(param) == Pecahan:
            the_lcm = lcm(self.denom, param.denom)
            numerator_diff = (the_lcm * self.numer // self.denom) - \
                (the_lcm * param.numer // param.denom)
            return Pecahan(numerator_diff, the_lcm)
        else:
            print("Wrong Type")
            raise(TypeError)
        
    def reduce(self):
        """ Return the reduced Pecahan """
        # find the gcd and then divide numerator and denominator by gcd
        the_gcd = gcd(self.numer, self.denom)
        return Pecahan(self.numer // the_gcd, self.denom // the_gcd)
    
    def __eq__(self, param):
        if type(param) == int:
            param = Pecahan(param)
        """ Compare two Pecahans for equality, return Boolean"""
        # reduce both; then check that numerators and denominators are equal
        reduced_self = self.reduce()
        reduced_param = param.reduce()
        return reduced_self.numer == reduced_param.numer and \
            reduced_self.denom == reduced_param.denom
    
    def __radd__(self, param):
        """ Add two Pecahans, with arguments reversed """
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to param
        # mapping is already reversed so self will be Pecahan; call __add__
        return self.__add__(param)
    
    def __mul__(self, param):
        # multiply two Pecahans
        if type(param) == int: # if parameter is an integer
            param = Pecahan(param) # Convert integer to Pecahan form
         
        multiply_numer = self.numer * param.numer   # Multiply two Pecahan's numerator
        multiply_denom = self.denom * param.denom   # Multiply two Pecahan's denominator

        return Pecahan(multiply_numer, multiply_denom)
    
    def __rmul__(self, param):
        # multiplication mapping is reversed
        return self.__mul__(param)
    
    def __truediv__(self, param):
        # Divide two Pecahan
        if type(param) == int: # Convert integer to Pecahan
            param = Pecahan(param)
        if type(param) == Pecahan:     
            # Two divide Pecahan, the param is flipped and multiplied by self       
            flipped_param = Pecahan(param.denom, param.numer)
            return self.__mul__(flipped_param)
        else:
            print('Wrong Type')
            return(TypeError)

    def __rtruediv__(self, param):
        # Division mapping is flipped
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:            
            self = Pecahan(self.denom, self.numer)
            return self.__mul__(param)
        else:
            print('Wrong Type')
            return(TypeError)
    
    def __gt__(self, param):
        # Compare if Pecahan is greater than other Pecahan
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            # normalize two Pecahan
            denom_lcm = lcm(self.denom, param.denom)
            
            # normalized Pecahan
            normalized_self = Pecahan(self.numer * (denom_lcm // self.denom), denom_lcm)
            normalized_param = Pecahan(param.numer * (denom_lcm // param.denom), denom_lcm)

            if normalized_self.numer > normalized_param.numer:
                return(True)
            else:
                return(False)
        else:
            print('Wrong Type')
            return(TypeError)
        
    def __ge__(self, param):
        # Same logic with __gt__ but use >= instead of >
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:                
            denom_lcm = lcm(self.denom, param.denom)
            normalized_self = Pecahan(self.numer * (denom_lcm // self.denom), denom_lcm)
            normalized_param = Pecahan(param.numer * (denom_lcm // param.denom), denom_lcm)

            if normalized_self.numer >= normalized_param.numer:
                return(True)
            else:
                return(False)
        else:
            print('Wrong Type')
            return TypeError
        
    def __getitem__(self, index):
        # Firstly, check if index is integer
        if type(index) == int:
            if index == 1:
                return self.numer
            elif index == 2:
                return self.denom
            else:
                raise(ValueError)
        # If not, return TypeError
        else:
            print('Wrong Index Type')
            print(TypeError)

def main():
    p1 = Pecahan(3,5)
    p2 = Pecahan(1,20)

    print( Pecahan(8,1) ) # 8
    print( p1*p2 ) # 3/100
    print( p1/p2 ) # 60/5
    print( p1*3 ) # 9/5
    print( 3*p1 ) # 9/5
    print( p1[1] ) # 3
    print( p1[2] ) # 5
    print( p1 > p2 ) # True
    print( p2 > p1 ) # False
    print( Pecahan(1,2) >= Pecahan(3,6) ) # True
    print( Pecahan(50,101)[2] ) # 101
    print( Pecahan(2,5) > Pecahan(4,5) ) # False
    print( Pecahan(3,7) >= Pecahan(1,7)*3 ) # True

    print( Pecahan(3,7)/3 == Pecahan(1,7) ) # True

    print( Pecahan(9,20)*Pecahan(20,9) ) # 180/180
    print( (Pecahan(9,20)*Pecahan(20,9)).reduce() ) # 1
    print( Pecahan(29,100003).reduce() ) # 29/100003
    print( Pecahan(2,3).__repr__() ) # Pecahan(2,3)

    # print( p1[0] ) # will generate exception ValueError

if __name__ == '__main__':
    main()