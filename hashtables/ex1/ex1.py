def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    # instantiate a dictionary
    weights_dict = dict()

    # iterate over the weigths list
    for i in range(length):
        # check if a key value pair is already contained in the dictionary
        # that matches the remainder of the subtraction of the current
        # element from the limit
        y = weights_dict.get(limit - weights[i])
        # if a value is found at that index in the dictionary
        if y != None:
            # return a tuple with the corresponding indexes
            return (i, y)
        else:
            # if not found, then set the key as the current value
            # from the weight list and the value as the index at which is found
            weights_dict[weights[i]] = i

    print(weights_dict)
    # if the sum of the num in the weight list does not 
    # add up to the limit, return None
    return None

# get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)