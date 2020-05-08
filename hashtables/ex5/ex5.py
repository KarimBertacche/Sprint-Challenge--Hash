def finder(files, queries):

    """
    YOUR CODE HERE
    """
    files_dict = dict()
    result = list()

    for q in queries:
        files_dict[q] = list()

    for idx, file in enumerate(files):
        path = file.split('/')[-1]
        if path in files_dict:
            files_dict[path].append(file)
            result.append(file)
        else:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))