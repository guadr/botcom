import adafruit_gps
import serial
import sys

class GuadrPS(object):
    def __init__(self):
        try:
            self.uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
        except (serial.serialutil.SerialException, FileNotFoundError):
            sys.exit("GPS device not found. Try again.")

        self.device = adafruit_gps.GPS(self.uart, debug=False) 
        self._configure() 


    def _configure(self):
        """TODO: add different configurations"""
        # Turn on the basic GGA and RMC info
        self.device.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        # Set update rate to once a second (1hz)
        self.device.send_command(b'PMTK220,1000')

    def update(self):
        if self.device.has_fix:
            self.device.update()

            self.lat = self.device.latitude
            self.long = self.device.long
            self.device_time = '{}/{}/{} {:02}:{:02}:{:02}'.format(
                gps.timestamp_utc.tm_mon,
                gps.timestamp_utc.tm_mday,
                gps.timestamp_utc.tm_year,
                gps.timestamp_utc.tm_hour,
                gps.timestamp_utc.tm_min,
                gps.timestamp_utc.tm_sec)

    def get_loc(self):
        return tuple(self.lat, self.lon)
