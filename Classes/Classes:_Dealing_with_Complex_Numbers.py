"""

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Input Format

One line of input: The real and imaginary part of a number separated by a space.

Output Format

For two complex numbers
and

, the output should be in the following sequence on separate lines:


For complex numbers with non-zero real
and complex part, the output should be in the following format:

Replace the plus symbol with a minus symbol when

.

For complex numbers with a zero complex part i.e. real numbers, the output should be:
For complex numbers where the real part is zero and the complex part is non-zero, the output should be:

Sample Input

2 1
5 6

Sample Output

7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i

Concept

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here.

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

__add__-> Can be overloaded for + operation


__sub__ -> Can be overloaded for - operation


__mul__ -> Can be overloaded for * operation



For more information on operator overloading in Python, refer here.


"""

# solution 1

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a + b).real, (a + b).imag).__str__()

    def __sub__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a - b).real, (a - b).imag).__str__()

    def __mul__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a * b).real, (a * b).imag).__str__()

    def __truediv__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a / b).real, (a / b).imag).__str__()

    def mod(self):
        return Complex(abs(complex(self.real, self.imaginary)), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result





#####################################################################################
#####################################################################################

class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


# solution 2
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a + c, b + d)

    def __sub__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a - c, b - d)

    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_mult = (a * c) - (b * d)
        imag_mult = (a * d) + (b * c)
        return Complex(real_mult, imag_mult)

    def __div__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_numerator = a * c + b * d
        imag_numerator = b * c - a * d
        denom = c * c + d * d
        real_div = real_numerator / denom
        imag_div = imag_numerator / denom
        return Complex(real_div, imag_div)

    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt(a ** 2 + b ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result









