class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []

    ticketsTable = {}

    for ticket in tickets:
        ticketsTable[ticket.source] = ticket.destination

    startingTicket = ticketsTable.get("NONE")
    endingTicket = [k for k, v in ticketsTable.items() if v == "NONE"][0]

    current = startingTicket
    while (current != endingTicket):
        route.append(current)
        current = ticketsTable.get(current)

    route.append(current)
    route.append("NONE")

    return route
