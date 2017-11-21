import random
import config

class Event:

    """ Defined inner class, Ticket 
    
    """
    class Ticket:

        def __init__(self):
            # "Each ticket has a non-zero price, expressed in US Dollars."
            # Assume that each ticket has price between 1 and 50 US Dollars.
            self.price = float("{0:.2f}".format(random.uniform(1, 50)))

        def __lt__(self, other):
            return self.price < other.price

        def __str__(self):
            return self.format_price(str(self.price))

        def format_price(self, price):
            split = price.split('.')
            dollars = split[0].zfill(2)
            pennies = split[1].ljust(2, '0')
            return '${}.{}'.format(dollars, pennies)

    def __init__(self):
        # "Each event has a unique numeric identifier between 1 and 3."
        self.nid = random.randint(1, 3)
        
        # "Each event has zero or more tickets."
        # Assume that each event can hold a maximum of 10 tickets.
        self.tickets = [self.Ticket() for _ in range (random.randint(0, 10))]
        # Assume that ticket list is sorted in terms of their price.
        self.tickets.sort()

        #self.pos = pos
        
    def __str__(self):
        padded_nid = str(self.nid).zfill(config.padding_size)
        min_price = 0 if not self.tickets else self.tickets[0]
        dist = 0

        return 'Event {} - {}, Distance {}'.format(padded_nid, min_price, dist)

