def finder(files, queries):

    """
    YOUR CODE HERE
    """
    files_dict = dict()
    result = list()

    for idx, file in enumerate(files):
        for q in queries:
            if q in files[idx]:
               files_dict[idx] = file 

    for idx in files_dict:
        result.append(files[idx])

    print(result)

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

# finder(files, queries)

# first solution, very slow for very large file size

# for q in queries:
#     for idx, file in enumerate(files):
#         path = file.split('/')[1:]
#         if q in path:
#             files_dict[idx] = file

# for idx in files_dict:
#     result.append(files[idx])