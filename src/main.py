from grid import Grid

if __name__ == "__main__":
    
    coordinates = input('Please Input Coordinates: ')
    grid = Grid(coordinates)
    grid.find_closest_events()

