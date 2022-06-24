def isValidVectorValue(a) -> bool:
    if (not isinstance(a, list)):
        return False
    for element in a:
        if (not isinstance(element, float) and not isinstance(element, int)):
            return False
    return True


def assertVectorValue(a):
    if (not isValidVectorValue(a)):
        raise TypeError("Un vector debe tener cómo valor una lista de números decimales o enteros")


def assertOperability(a: 'Vector', b: 'Vector'):
    if (a.dimension != b.dimension):
        raise TypeError("Vectors must be equal")


class Vector:
    def __init__(self, list: list) -> None:
        assertVectorValue(list)
        self.values = list
        self.dimension = len(list)
        pass

    def __eq__(A, B: 'Vector') -> 'bool':
        if (A.dimension != B.dimension):
            return False
        if (A.values != B.values):
            return False
        return True

    def __add__(A, B: 'Vector') -> 'Vector':
        assertOperability(A, B)

        c = []
        a, b = A.values, B.values

        for i in range(A.dimension):
            c_i = a[i] + b[i]
            c.append(c_i)

        return Vector(c)

    def __sub__(A, B: 'Vector') -> 'Vector':
        assertOperability(A, B)

        c = []
        a, b = A.values, B.values
        for i in range(A.dimension):
            c_i = a[i] - b[i]
            c.append(c_i)

        return Vector(c)

    def __matmul__(A, B: 'Vector'):
        assertOperability(A, B)

        res = 0
        a, b = A.values, B.values
        for i in range(A.dimension):
            res += a[i]*b[i]

        return res


if(__name__ == "__main__"):
    a = [1, 2, 3, 4]
    assert(isValidVectorValue(a))

    a = [.1, .2, .3, .4]
    assert(isValidVectorValue(a))

    a = [1, .2, .1, 5]
    assert(isValidVectorValue(a))

    a = ["1", "2", "3"]
    assert(not isValidVectorValue(a))

    a = Vector([1]*3)
    b = Vector([2]*3)

    c = a+b
    assert(c == Vector([3]*3))
    c = b-a
    assert(c == Vector([1]*3))

    c = b@a
    assert(c == 2*3)

    a = Vector([1, 2, 3])
    b = Vector([4, 5.0, 6])

    c = a+b
    assert(c == Vector([5, 7.0, 9]))

    c = a-b
    assert(c == Vector([-3, -3.0, -3]))

    c = a@b
    assert(c == (4 + 10.0 + 18))

    a = Vector([1, 2, .5])
    b = Vector([2, 3, 4])
    c = a@b
    assert(c == (2+6+2))
