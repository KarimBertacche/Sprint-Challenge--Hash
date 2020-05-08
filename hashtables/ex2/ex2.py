#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    # initialize an instance of a dictionary to store the routes 
    trips_dict = dict()
    # initialize a list where to store the final ordered list
    flight_routes = list()

    # iterate over each ticket
    for ticket in tickets:
        # set the ticket source as key in dict and destination as the value
        trips_dict[ticket.source] = ticket.destination

    # set an index to loop over the list
    idx = 0
    # set the current destination to initialize the list
    current_destination = "NONE"

    # iterate while there are tickets
    while idx < length:
        # set the current destination to be the new source of the next iteration
        current_destination = trips_dict.get(current_destination)
        # append on each iteration the ordered routes by first to last
        flight_routes.append(current_destination)
        # # move to next iteration
        idx += 1

    # return the ordered flight routes at the end
    return flight_routes