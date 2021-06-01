def flatten1(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested1 = [[1, 2], [3, 4], [5]]
print(list(flatten1(nested1)))


def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested


nested2 = [[[1], 2], 3, 4, [5, [6, 7]], 8]
print(list(flatten2(nested2)))


def flatten3(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield nested


nested3 = ['foo', ['bar', ['baz']]]
print(list(flatten3(nested3)))
