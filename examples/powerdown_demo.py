# A demo to show off power-down mode
# Author: Blake Felt

import time
import Adafruit_MCP4725

dac = Adafruit_MCP4725.MCP4725()

voltage = 4095 # voltage to write for demo
sleep_time = 2 # time to pause between commands

modes = [1,100,500] # all available shutdown modes (see datasheet)

for i in modes: # for every mode
    dac.set_voltage(voltage) # turn on device
    print 'turned on device'
    time.sleep(sleep_time) 
    resistor = dac.power_down(i) # enter power-down mode with the set resistor
    print 'Entered power-down mode with {0}kOhm resistor'.format(resistor)
    time.sleep(sleep_time)

dac.power_down() # defaults to 1 kOhm resistor
