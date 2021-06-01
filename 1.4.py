import operatordef

mergeiter(*iterables, **kwargs):
iterables = [iter(it) for it in iterables]
iterables = {i: [next(it), i, it] for i, it in enumerate(iterables)}
if 'key' not in kwargs:
    key = operator.itemgetter(0)
else:
    key = lambda item, key=kwargs['key']: key(item[0])

while True:
    value, i, it = min(iterables.values(), key=key)
    yield value
    try:
        iterables[i][0] = next(it)
    except StopIteration:
        del iterables[i]
        if not iterables:
            raise
