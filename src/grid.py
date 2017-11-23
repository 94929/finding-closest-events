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
    # User input coordinates.
    coordinates = (None, None)
    
    # Our environment has 21x21 grid.
    grid = {}
    
    # This is a list containing all events generated in the grid.
    events = []


    def init_grid(coordinates):
        # TODO what if input is like "helhlehoe"?
        origin_x, origin_y = tupler.literal_eval(coordinates)

        # TODO Check if the translated co-ordinates are valid or not.
        if not Grid.validate_coordinates(origin_x, origin_y):
            print ('Please input valid co-ordinates...')
            return
        
        # Once we know the coordinates are valid, we translate it into grid.
        trans_x, trans_y = Grid.translate_coordinates(origin_x, origin_y)

        # Assign valid coordinates.
        coordinates = trans_x, trans_y

        # Create grid according to the specification.
        #grid = np.zeros(shape=[config.width*2+1, config.height*2+1])

        Grid.init_event()
    
    # The distance between two points should be computed as the Manhattan distance.
    def calculate_distance(src, dst):
        pass

    def validate_coordinates(x, y):
        return -config.width <= x <= config.width and -config.height <= y <= config.height

    def translate_coordinates(x, y):
        return x + config.offset, y + config.offset
   
    # Initialise events and put them into the environment.
    def init_event():
        # Randomly generate and assign events for nb_events times.
        # Assume we have total 50 events in our environment.
        for _ in range(config.nb_events):
            rand_x = random.randint(-config.width, config.width)
            rand_y = random.randint(-config.height, config.height)
            location = rand_x, rand_y
            grid[location] = Event()

