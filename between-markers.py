def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # return text[text.find(begin) + len(begin) if text.find(begin) != -1 else 0: text.find(end) if text.find(
    #     end) != -1 else len(text)]

    # your code here
    begin_index = text.find(begin)
    begin_len = len(begin)
    end_index = text.find(end)
    end_len = len(end)
    if begin_index == -1 and end_index == -1:
        return text
    elif begin_index == -1 and end_index > -1:
        return text[:end_index]
    elif end_index == -1 and begin_index > -1:
        return text[begin_index + begin_len:]
    elif begin_index > end_index:
        return ''
    else:
        return text[begin_index + begin_len:end_index]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
