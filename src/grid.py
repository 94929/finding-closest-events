import sys
import ast as tupler
import random
import config

from event import Event


# I could have used singleton pattern to ensure there is only one instance of Grid
class Grid:
    
    def __init__(self, coordinates):
        try:
            trimmed_coordinates = coordinates.strip()
            self.coordinates = self.validate_coordinates(trimmed_coordinates)
        except:
            print('Please input a valid form of co-ordinates.')
            sys.exit()

        # The dictionary grid works as our world.
        # It provides the same environment as 2D array but better performance.
        self.grid = {}

        # Create a list for tracking nids of the events
        self.nids = []

        # Then help initialising grid by creating new events in the world.
        self.create_events()
        
    # This returns(prints to the console) a list of the five closest events.
    def find_closest_events(self):
        five_closest_distances = self.calculate_distances()[:config.nb_closest_events]
        five_closest_locations = [location for location, _ in five_closest_distances]
        five_closest_events = [self.grid[location] for location in five_closest_locations]
        
        print('Closest Events to {}:'.format(self.coordinates))
        for i in range(config.nb_closest_events):
            event = five_closest_events[i]
            distance = five_closest_distances[i][1]
            print('{}, Distance {}'.format(event, distance))

    # This returns a list of distances with corresponding locations.
    def calculate_distances(self):
        distances = []
        for location in self.grid:
            distance = self.calculate_distance(self.coordinates, location)
            distances.append((location, distance))

        # Before return, it sorts the list by tuple value (i.e. distance)
        distances = sorted(distances, key=lambda x: x[1])
        return distances

    # The distance between two points should be computed as the Manhattan distance.
    def calculate_distance(self, src, dst):
        # Manhattan distance = |Ax - Bx| + |Ay - By|
        return abs(src[0] - dst[0]) + abs(src[1] - dst[1])

    # Check if the user input is valid or not.
    def validate_coordinates(self, coordinates):
        x, y = tupler.literal_eval(coordinates)
        w, h = config.width, config.height
        
        if not (-w <= x <= w and -h <= y <= h):
            raise Exception
        
        return x, y

    # Initialise events and put them into the environment.
    def create_events(self):
        # Randomly generate and assign events for nb_events times.
        # Assume we have total 10 events in our environment.
        for _ in range(config.nb_events):
            # Assume that the same random location will not be generated.
            rand_x = random.randint(-config.width, config.width)
            rand_y = random.randint(-config.height, config.height)
            location = rand_x, rand_y

            # Generate nid
            nid = self.generate_nid()
            self.nids.append(nid)

            # Assign an event to the location given.
            self.grid[location] = Event(nid)
    
    def generate_nid(self):
        # For each event, this function generates appropriate nid.
        return len(self.nids)+1

