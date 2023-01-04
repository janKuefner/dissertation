from smbus import SMBus  # necessary for I2C communication
import time  # necessary for I2 communication


def initialize_I2Cs():
    #  initializing I2C adress 0x20
    '''I2C address 0x20, side A, GPIOs set to output'''
    i2cbus.write_word_data(0x21, 0x00, 0x00)
    '''I2C address 0x20, side B, GPIOs set to output'''
    i2cbus.write_word_data(0x21, 0x01, 0x00)


def switch_module_pin(module, pin):
    # general times
    time_actuator_on = 0.1   # time the actuator is powered
    time_actuator_off = 0.001  # time the actuator is off
    # provide the module I2C adress as hex value
    if module == 1:
        i2caddress = 0x20
    elif module == 2:
        i2caddress = 0x21
    elif module == 3:
        i2caddress = 0x22
    else:
        print("error")
    # provide pin and side as hex value
    if pin == 0:
        pin_hex = 0x00
        A_or_B_side = 0x12
    elif pin == 1:
        pin_hex = 0x01
        A_or_B_side = 0x12
    elif pin == 2:
        pin_hex = 0x02
        A_or_B_side = 0x12
    elif pin == 3:
        pin_hex = 0x04
        A_or_B_side = 0x12
    elif pin == 4:
        pin_hex = 0x08
        A_or_B_side = 0x12
    elif pin == 5:
        pin_hex = 0x10
        A_or_B_side = 0x12
    elif pin == 6:
        pin_hex = 0x20
        A_or_B_side = 0x12
    elif pin == 7:
        pin_hex = 0x40
        A_or_B_side = 0x12
    elif pin == 8:
        pin_hex = 0x80
        A_or_B_side = 0x12
    elif pin == 9:
        pin_hex = 0x01
        A_or_B_side = 0x15
    elif pin == 10:
        pin_hex = 0x02
        A_or_B_side = 0x15
    elif pin == 11:
        pin_hex = 0x04
        A_or_B_side = 0x15
    elif pin == 12:
        pin_hex = 0x08
        A_or_B_side = 0x15
    elif pin == 13:
        pin_hex = 0x10
        A_or_B_side = 0x15
    elif pin == 14:
        pin_hex = 0x20
        A_or_B_side = 0x15
    elif pin == 15:
        pin_hex = 0x40
        A_or_B_side = 0x15
    elif pin == 16:
        pin_hex = 0x80
        A_or_B_side = 0x15
    else:
        raise ValueError("This pin number is not defined")
    sent = False
    while (sent == False):
        try:
            i2cbus.write_byte_data(i2caddress, A_or_B_side, pin_hex)
            print("on")
            time.sleep(time_actuator_on)
            sent = True
        except OSError:
            sent = False
    sent = False
    while (sent == False):
        try:
            i2cbus.write_byte_data(i2caddress, 0x12, 0x00)
            time.sleep(time_actuator_off / 2)
            sent = True
        except OSError:
            sent = False
    sent = False
    while (sent == False):
        try:
            i2cbus.write_byte_data(i2caddress, 0x15, 0x00)
            time.sleep(time_actuator_off / 2)
            sent = True
        except OSError:
            sent = False


if __name__ == "__main__":
    i2cbus = SMBus(1)  # i2cbus object creation
    initialize_I2Cs()
    while (True):
        # module 1
        switch_module_pin(1, 1)
        switch_module_pin(1, 2)
        switch_module_pin(1, 3)
        switch_module_pin(1, 4)
        switch_module_pin(1, 5)
        switch_module_pin(1, 6)
        switch_module_pin(1, 7)
        switch_module_pin(1, 8)
        switch_module_pin(1, 9)
        switch_module_pin(1, 10)
        switch_module_pin(1, 11)
        switch_module_pin(1, 12)
        switch_module_pin(1, 13)
        switch_module_pin(1, 14)
        switch_module_pin(1, 15)
        switch_module_pin(1, 16)
        switch_module_pin(1, 0)  # no switching at all
        switch_module_pin(1, 0)  # no switching at all
        switch_module_pin(1, 0)  # no switching at all
        switch_module_pin(1, 0)  # no switching at all
        # module 2
        switch_module_pin(2, 1)
        switch_module_pin(2, 2)
        switch_module_pin(2, 3)
        switch_module_pin(2, 4)
        switch_module_pin(2, 5)
        switch_module_pin(2, 6)
        switch_module_pin(2, 7)
        switch_module_pin(2, 8)
        switch_module_pin(2, 9)
