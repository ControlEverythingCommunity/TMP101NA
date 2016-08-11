# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TMP101NA
# This code is designed to work with the TMP101NA_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=TMP101NA_I2CS#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# TMP101NA address, 0x49(73)
# Select configuration register, 0x01(1)
#		0x60(96)	Continous conversion, Comparator mode
#					Polarity Active low, 12-Bit Resolution
i2c.writeByte(0x49, 0x01, 0x60)

time.sleep(0.5)

# TMP101NA address, 0x49(73)
# Read data back from 0x00(0), 2 bytes
# cTemp MSB, cTemp LSB
data = i2c.readBytes(0x49, 0x00, 2)

# Convert the data to 12-bits
cTemp = (data[0] * 256 + (data[1] & 0xF0)) / 16
if cTemp > 2047 :
	cTemp -= 4096
cTemp = cTemp * 0.0625
fTemp = cTemp * 1.8 + 32

# Output data to screen
print "Temperature in Celsius is : %.2f C" %cTemp
print "Temperature in Fahrenheit is : %.2f F" %fTemp
