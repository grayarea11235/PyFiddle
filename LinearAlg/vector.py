import operator

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def add(self, v):
        return tuple(map(operator.add, self.coordinates, v.coordinates))

    def sub(self, v):
        return tuple(map(operator.sub, self.coordinates, v.coordinates))

    def scale(self, s):
        return tuple(s*x for x in self.coordinates)

    def mag(self):
        pass

    def norm(self):
        pass


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


def my_code():
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



my_code()