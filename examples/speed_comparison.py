# A speed comparison of the set_voltage and set_fast commands
# Sets voltage from 0 to Vdd, then prints time taken
# Author: Blake Felt

import time
import Adafruit_MCP4725

# create dac instance
dac = Adafruit_MCP4725.MCP4725()

max_volts = 4095

print 'Press ctrl+C to quit:'
while True:
    tic1 = time.time() # find current time
    for i in xrange(max_volts+1): # for every voltage value
        dac.set_voltage(i) # set voltage
    toc1 = time.time()-tic1 # find time elapsed

    tic2 = time.time()
    for i in xrange(max_volts+1):
        dac.set_fast(i)
    toc2 = time.time()-tic2
    
    # print times
    print 'It took {0} seconds to write every voltage with set_voltage'.format(toc1)
    print 'It took {0} seconds to write every voltage with set_fast\n'.format(toc2)
