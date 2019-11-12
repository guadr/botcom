class Location(object);
    def __init__(self, lon, lat):
        self._lon = lon
        self._lat = lat

    def get_loc(self):
        return tuple(self._lat, self._lon)
