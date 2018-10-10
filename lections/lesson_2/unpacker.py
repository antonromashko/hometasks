def unpacker(*args):
    result = []
    for arg in args:
        if isinstance(arg, (tuple, list, set, frozenset)):
            result.extend(unpacker(*arg))
        else:
            result.append(arg)
    return result


print(unpacker(1,2,3,[4,5,[6,7,[8]]]))
