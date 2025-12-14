from math import hypot, atan, sin, cos

class CustomComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.__class__(self.real, -self.imag)

    def argz(self):
        return atan(self.imag / self.real)

    def __abs__(self):
        return hypot(self.real, self.imag)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.real}, {self.imag})"

    def __str__(self):
        return f"({self.real}{self.imag:+}j)"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            real = self.real + other
            imag = self.imag
        elif isinstance(other, self.__class__):
            real = self.real + other.real
            imag = self.imag + other.imag
        else:
            raise TypeError
        return self.__class__(real, imag)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            real = self.real - other
            imag = self.imag
        elif isinstance(other, self.__class__):
            real = self.real - other.real
            imag = self.imag - other.imag
        else:
            raise TypeError
        return self.__class__(real, imag)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            real = self.real * other
            imag = self.imag * other
        elif isinstance(other, self.__class__):
            real = (self.real * other.real) - (self.imag * self.imag)
            imag = (self.real * other.imag) + (self.imag * other.real)
        else:
            raise TypeError
        return self.__class__(real, imag)

    def __radd__(self, other):
        return self+other

    def __rmul__(self, other):
        return self*other

    def __rsub__(self, other):
        # In case other is CustomComplex -> handled by __sub__
        if not isinstance(other, (int, float)):
            raise TypeError
        real = other - self.real
        imag = -self.imag

        return self.__class__(real, imag)

    def __eq__(self, other):
        if (self.real == other.real) and (self.imag == other.imag):
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __pow__(self, other):
        r_raised = abs(self) ** other
        argz_multiplied = self.argz() * other

        real_part = round(r_raised * cos(argz_multiplied))
        imag_part = round(r_raised * sin(argz_multiplied))

        return self.__class__(real_part, imag_part)
