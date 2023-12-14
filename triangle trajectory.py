#!/usr/bin/env python
import time
import argparse
from flyt_python import api

def main():
    drone = api.navigation(timeout=120000) 

    # at least 3sec sleep time
    time.sleep(3)

    # parsing command line arguments
    parser = argparse.ArgumentParser(description='Process a float value.')
    parser.add_argument('side', metavar='side_length', type=float, help='side length of the triangle')
    args = parser.parse_args()

    # lets fly
    side_length = args.side
    altitude = 10.0

    print("taking off!")
    drone.take_off(altitude)

    print('flying in triangle with side length', side_length, 'and height', altitude)
    # Fly in a triangular trajectory
    drone.position_set(10, 0, 0, relative=True)    # Move to the first vertex
    drone.position_set(-10/2, 10* 3**0.5/2, 0, relative=True) # Move to the second  vertex
    drone.position_set(-10/2, -10* 3**0.5/2, 0, relative=True) # Move to the third vertex
    
    print("landing")
    drone.land(False)
    
    # shutdown the instance
    drone.disconnect()

if __name__ == "__main__":
    main()
