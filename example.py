#!/usr/bin/env python3
import logging
from ina226 import INA226
from time import sleep


def read():
    print("Bus Voltage    : %.3f V" % ina.voltage())
    print("Bus Current    : %.3f mA" % ina.current())
    print("Supply Voltage : %.3f V" % ina.supply_voltage())
    print("Shunt voltage  : %.3f mV" % ina.shunt_voltage())
    print("Power          : %.3f mW" % ina.power())


if __name__ == "__main__":
    ina = INA226(busnum=1, max_expected_amps=25, log_level=logging.DEBUG)
    ina.configure()
    ina.set_low_battery(5)
    sleep(3)
    print("===================================================Begin to read")
    read()
    sleep(2)
    '''
    print("===================================================Begin to reset")
    ina.reset()
    sleep(5)
    ina.configure()
    ina.set_low_battery(3)
    sleep(5)
    print("===================================================Begin to sleep")
    ina.sleep()
    sleep(2)
    print("===================================================Begin to wake")
    ina.wake()
    sleep(0.2)
    print("===================================================Read again")
    read()
    sleep(5)
    print("===================================================Trigger test")
    '''
    ina.wake(3)
    sleep(0.2)
    while True:
        ina.wake(3)
        sleep(3)
        while 1:
            if ina.is_conversion_ready():
                sleep(3)
                print("===================================================Conversion ready")
                read()
                break
        sleep(1)
        print("===================================================Trigger again")
