import numpy as np
import ast as tupler
import random
import config

from event import Event


""" Create static class, Grid.
    Grid should be static as we only need one instance of this.
    Could have used singleton pattern to achieve the goal but that's overwhelming.
"""
class Grid:
    coordinates = (None, None)
    
    # Using a dictionary gives us a virtual experience on our program.
    # This acts like the worlds operates within a range from -10 to 10 in x, y axis.
    grid = {}
    
    def init_grid(coordinates):
        # TODO what if input is like "helhlehoe"?
        origin_x, origin_y = tupler.literal_eval(coordinates)
        print(origin_x, origin_y)
        # TODO Check if the translated co-ordinates are valid or not.
        if not Grid.validate_coordinates(origin_x, origin_y):
            print ('Please input valid co-ordinates...')
            return
        
        # Assign valid coordinates.
        Grid.coordinates = origin_x, origin_y

        Grid.create_events(Grid.grid)
    
    # This returns a list of the five closest events.
    def find_closest_events():
        five_closest_distances = Grid.calculate_distances()[:5]
        five_closest_locations = [location for location, _ in five_closest_distances]
        five_closest_events = [Grid.grid[location] for location in five_closest_locations]
        
        print('Closest Events to {}:'.format(Grid.coordinates))
        for i in range(config.nb_closest_events):
            event = five_closest_events[i]
            distance = five_closest_distances[i][1]
            print(event)

    # This returns a list of distances with corresponding locations.
    def calculate_distances():
        distances = []
        for location in Grid.grid:
            distance = Grid.calculate_distance(Grid.coordinates, location)
            distances.append((location, distance))

        # Before return, it sorts the list by tuple value (i.e. distance)
        distances = sorted(distances, key=lambda x: x[1])
        return distances


    # The distance between two points should be computed as the Manhattan distance.
    def calculate_distance(src, dst):
        src_x = src[0]
        src_y = src[1]
        dst_x = dst[0]
        dst_y = dst[1]

        return abs(src_x - dst_x) + abs(dst_x - dst_y)

    def validate_coordinates(x, y):
        return -config.width <= x <= config.width and -config.height <= y <= config.height

    # Initialise events and put them into the environment.
    def create_events(grid):
        # Randomly generate and assign events for nb_events times.
        # Assume we have total 50 events in our environment.
        for _ in range(config.nb_events):
            # Assume that the same random location will not be generated.
            rand_x = random.randint(-config.width, config.width)
            rand_y = random.randint(-config.height, config.height)
            location = rand_x, rand_y
            grid[location] = Event()

