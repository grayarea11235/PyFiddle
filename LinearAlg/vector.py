import operator
from math import sqrt, acos, pi
from decimal import Decimal, getcontext


# This class was developed while doing the Udacity linear algerbra refresher free course.
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def add(self, v):
        return Vector(tuple(map(operator.add, self.coordinates, v.coordinates)))


    def sub(self, v):
        return Vector(tuple(map(operator.sub, self.coordinates, v.coordinates)))


    def scale(self, s):
        return Vector(tuple(s*x for x in self.coordinates))


    def mag(self):
        return sqrt(sum(x*x for x in self.coordinates))


    def dot(self, v):
        return sum(x*y for x, y in zip(self.coordinates, v.coordinates))


    def norm(self):
        a = self.scale(Decimal(1.0) / Decimal(self.mag()))
        return a


    def angle_with(self, v, in_degrees = False):
        #try:
        u1 = self.norm()
        u2 = v.norm()
        res = acos(u1.dot(u2))

        if in_degrees == True:
            res = rad2deg(res)

        return res
        #except:
        #    print('Do exception handling here')



    def is_parallel(self, v):
        #print(self.angle_with(v))
        return (self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi) # due to imprecision this doesnt really work - FIXIT

        a = tuple(map(operator.truediv, self.coordinates, v.coordinates))
#        print(a)

    def is_orthogonal(self, v, tolerance=1e-10):
        s = abs(self.dot(v))
        if s < tolerance:
            return True

        return False

    def is_zero(self, tolerance=1e-10):
        return self.mag() < tolerance


    def proj(self, v):
        dp = self.dot(v)
        m = self.mag() ** 2
        r = (dp / m)
        return self.scale(r)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


def rad2deg(rads):
    return (rads * 180.) / pi



# Test below

def my_code1():
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])
    v3 = v1.add(v2)

    print('First result = {0!s}'.format(v3))

    v1 = Vector([7.119, 8.215])
    v2 = Vector([-8.223, 0.878])
    v3 = v1.sub(v2)

    print('Second result = {0!s}'.format(v3))

    v1 = Vector([1.671, -1.012, -0.318])
    s = 7.41
    v3 = v1.scale(s)

    print('Third result = {0!s}'.format(v3))

def mini_test():
    v1 = Vector([1, 1, 1])
    v2 = Vector([2, 2, 2])
    v3 = Vector([4, 2, 3])
    s = 7

    print(v1.add(v2))
    print(v2.sub(v3))
    print(v1.scale(s))




def my_code2():
    v1 = Vector([-0.221, 7.437])
    print(v1.mag())

    v1 = Vector([8.813, -1.331, -6.247])
    print(v1.mag())

    v1 = Vector([5.581, -2.136])
    print(v1.norm())

    v1 = Vector([1.996, 3.108, -4.554])
    print(v1.norm())


def my_code3():
    v1 = Vector([1, 2, -1])
    v2 = Vector([3, 1, 0])
#    print(v1.dot(v2))
#    print(v1.angle_with(v2))

    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])
    print(v1.dot(v2))

    v1 = Vector([3.183, -7.627])
    v2 = Vector([-2.668, 5.319])
    print(v1.angle_with(v2))

    v1 = Vector([-5.955, -4.904, -1.874])
    v2 = Vector([-4.496, -8.755, 7.103])
    print(v1.dot(v2))

    v1 = Vector([7.35, 0.221, 5.188])
    v2 = Vector([2.751, 8.259, 3.985])
    print(rad2deg(v1.angle_with(v2)))


def test_orth_para():
    v = Vector([-7.579, -7.880])
    w = Vector([22.737, 23.65])

    print(v.is_parallel(w))
    print(v.is_orthogonal(w))

    v = Vector([-2.029, 9.97, 4.172])
    w = Vector([-9.231, -6.639, -7.245])

    print(v.is_parallel(w))
    print(v.is_orthogonal(w))

    v = Vector([-2.328, -7.284, -1.214])
    w = Vector([-1.821, 1.072, -2.94])

    print(v.is_parallel(w))
    print(v.is_orthogonal(w))

    v = Vector([-2.328, -7.284, -1.214])
    w = Vector([0, 0])

    print(v.is_parallel(w))
    print(v.is_orthogonal(w))

def test_proj():
    pass

#test_orth_para()
