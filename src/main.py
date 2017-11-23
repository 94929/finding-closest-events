from event import Event
from grid import Grid

if __name__ == "__main__":
    #e = Event()
    #print(e)
    
    coordinates = input('Please Input Coordinates:')
    Grid.init_grid(coordinates)
    Grid.find_closest_events()

