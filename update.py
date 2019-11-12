import requests
import time
import sys

if len(sys.argv) != 3:
    sys.exit("Incorrect usage:\n\tpython3 update.py {endpoint}")

_ENDPOINT = sys.argv[1] 

def ping(coord):
    """Ping server with robots current location

    Args:
        coord: two-tuple containing (latitude, longitude) of type float

    """
    print(coord[0], coord[1])


def run():
    """Temporary function to spoof gps coordinates while we wait for gps module
    """
    with open("path.txt") as pathfile:
        for line in pathfile:
            coordinate = tuple(line.split(","))
            ping(coordinate[:2])
            time.sleep(5)

if __name__ == "__main__":
    run()
