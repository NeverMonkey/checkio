def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # a = text.find(symbol,text.find(symbol)+1)
    # return a if a !=-1 else None
    # your code here
    index_list = []
    for i in range(len(text)):
        if text[i] == symbol:
            index_list.append(i)
    if len(index_list) >= 2:
        return index_list[1]
    else:
        return None
    # try:
    #     return text.index(symbol, text.index(symbol) + 1)
    # except ValueError:
    #     return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
