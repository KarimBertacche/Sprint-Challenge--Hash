def intersection(arrays):

    """
    YOUR CODE HERE
    """
    # create instance of a dictionary to hold key being the num and value being the count
    items_count = dict()
    # initialize a result list to append intersections
    result = []

    # we iterate over the arrays list
    for i, num_list in enumerate(arrays):
        # and iterate over each list
        for y in num_list:
            # if the item has already a count present in the dictinary and the index is more than 1 than we want to increase the count
            if items_count.get(y) != None and i > 0:
                # we pass the num as key, and increase the current value by 1
                items_count[y] = items_count[y] + 1
            # else if the there is no entry with that number in dictionary and index is 1
            # meaning that we are still iterating over first array
            elif items_count.get(y) is None and i == 0: 
                # then we set the initial count to 1
                items_count[y] = 1
            else:
                continue
    
    # we iterate over each dictionary entry
    for num in items_count:
        # if the num count is equal to the array length
        if items_count[num] == len(arrays):
            # we append that to the num
            result.append(num)

    return result

# intersection([[1, 3, 5], [3, 5, 1], [5, 34, 3]])

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
