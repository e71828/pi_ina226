# pi_ina226
## Introduction
This Python library supports the [INA226](https://www.ti.com/lit/ds/symlink/ina226.pdf) voltage, current and power monitor from Texas Instruments with a Raspberry Pi using the I2C bus. The intent of the library is to make it easy to use the quite complex functionality of this sensor.

The library currently not only supports continuous reads of voltage and power, but also triggered reads.

The library supports the detection of overflow in the current/power calculations which results in meaningless values for these readings.

The low power mode of the INA226 is supported, so if only occasional reads are being made in a battery based system, current consumption can be minimised.

## Usage

keep waiting to continue

## Test 
### Preparing 
The library has been tested with the Raspi 4b+.

<img src="img/test_with_pi.jpg" width="360" height="480">

### Result
<img src="img/result.png" width="480" height="240">
