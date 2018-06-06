def best_stock(data):
    # your code here
    max_value=sorted(data.values())[-1]
    max_value_index=list(data.values()).index(max_value)
    # return max(data, key=data.__getitem__)
    dict.__getitem__()
    return list(data.keys())[max_value_index]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
