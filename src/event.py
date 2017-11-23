import random
import config

""" Event class contains all properties (e.g. numeric id, tickets etc).

"""
class Event:

    """ Define inner class, Ticket.
        Ticket class is not defined as outer class because 
        we are using it only in Event class in this situation. 
    """
    class Ticket:

        def __init__(self):
            # "Each ticket has a non-zero price, expressed in US Dollars."
            # Assume that each ticket has price between 1 and 50 US Dollars.
            self.price = float("{0:.2f}".format(random.uniform(config.min_price, config.max_price)))

        def __lt__(self, other):
            return self.price < other.price

        def __str__(self):
            return self.format_price(str(self.price))

        def format_price(self, price):
            split = price.split('.')
            dollars = split[0].zfill(config.min_dollars_len)
            pennies = split[1].ljust(config.max_pennies_len, '0')
            return '${}.{}'.format(dollars, pennies)

    def __init__(self):
        # "Each event has a unique numeric identifier between 1 and 3."
        self.nid = random.randint(config.min_nid, config.max_nid)
        
        # "Each event has zero or more tickets."
        # Assume that each event can hold a maximum of 10 tickets.
        self.tickets = [self.Ticket() for _ in range (random.randint(config.min_nb_tickets, config.max_nb_tickets))]
        # Assume that ticket list is sorted in terms of their price.
        self.tickets.sort()
        
    def __str__(self):
        padded_nid = str(self.nid).zfill(config.padding_size)
        min_price = 'No Ticket Available' if not self.tickets else self.tickets[0]

        return 'Event {} - {}'.format(padded_nid, min_price)

