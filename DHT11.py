
import sys
import Adafruit_DHT as dht
import time

import datetime

h,t = dht.read_retry(dht.DHT11, 11)
print('val=',h)

print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h)
