def has_negatives(a):

    """
    YOUR CODE HERE
    """
    # initialize a dictionary to hold all numbers in array
    num_dict = dict()
    # initialize a list to return found matches
    result = list()

    # iterate over each num in list
    for num in a:
        # if the num as a correspoding number in the dictionary
        if num_dict.get(abs(num)):
            # check if there sum adds up to 0
            if (num_dict.get(abs(num)) + num) == 0:
                # if so pass value to result list
                result.append(abs(num))
        else:
            # if no value is found, pass the num as new key
            # with its value
            num_dict[abs(num)] = num 

    # return result array
    return result

# has_negatives([-1,-2,1,2,3,4,-4])

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
