import requests
import time
import sys

from guadrps import GuadrPS

if len(sys.argv) != 3:
    sys.exit("Incorrect usage:\n\tpython3 update.py {username} {password}")

# TODO: refactor this whole script
_SESSION = requests.Session()
_AUTHENTICATED = False
_ENDPOINT = "http://0.0.0.0:5000/location/api/delivery/robot_location"
_CREDS = (sys.argv[1], sys.argv[2])


def authenticate():
    _SESSION.auth = _CREDS
    _AUTHENTICATED = True

def post_location(latitude, longitude, percent_complete):
    """Update server with robots current location

    Args:
        coord: two-tuple containing (latitude, longitude) of type float
    """
    _data = {
            "latitude": latitude, 
            "longitude": longitude,
            "perc_complete": percent_complete
    }
    _SESSION.post(_ENDPOINT, data=_data)     

def run():
    """R
    """
    if not _AUTHENTICATED:
        authenticate()

    gps = GuadrPS() 

    while True:
        if gps.device.has_fix:
            gps._update()
            post_location(gps.lat, gps.long)
            
        else:
            print("GPS has no fix......")

        time.sleep(1)
        
    """
    with open("path.txt") as pathfile:
        for line in pathfile:
            coordinate = tuple(line.split(","))
            ping(coordinate[:2])
            time.sleep(5)
    """

if __name__ == "__main__":
    run()
