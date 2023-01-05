from smbus import SMBus  # necessary for I2C communication
import time  # necessary for I2 communication


def initialize_I2Cs():
    #  initializing I2C adress 0x20
    '''I2C address 0x20, side A, GPIOs set to output'''
    i2cbus.write_word_data(0x20, 0x00, 0x00)
    '''I2C address 0x20, side B, GPIOs set to output'''
    i2cbus.write_word_data(0x20, 0x01, 0x00)
    #  initializing I2C adress 0x21
    '''I2C address 0x20, side A, GPIOs set to output'''
    i2cbus.write_word_data(0x21, 0x00, 0x00)
    '''I2C address 0x20, side B, GPIOs set to output'''
    i2cbus.write_word_data(0x21, 0x01, 0x00)
    #  initializing I2C adress 0x22
    '''I2C address 0x20, side A, GPIOs set to output'''
    i2cbus.write_word_data(0x22, 0x00, 0x00)
    '''I2C address 0x20, side B, GPIOs set to output'''
    i2cbus.write_word_data(0x22, 0x01, 0x00)


def switch_module_pin(module, pin):
    # general times the actuator stays actived / deactiveted
    time_actuator_on = 0.1   # time the actuator is powered. 0.1 is good
    time_actuator_off = 0.001  # time the actuator is off. 0.001 is good
    '''the following code switches on and off a certain actuator'''
    # get the module I2C adress as hex value
    if module == 1:
        i2caddress = 0x20
    elif module == 2:
        i2caddress = 0x21
    elif module == 3:
        i2caddress = 0x22
    else:
        print("error")
    # get the pin and side as hex value
    # A side = 0x12
    # B side = 0x15
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
    '''send hex values to chip in order to switch on the actuactor'''
    sent = False
    while (sent == False):
        try:
            i2cbus.write_byte_data(i2caddress, A_or_B_side, pin_hex)
            print("on")
            time.sleep(time_actuator_on)
            sent = True
        except OSError:
            sent = False
    ''' switch off A and B side'''
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


def switch_every_actuator_once():
    '''this function switches all actuators once. This function is sort of to
    help setting up or troubleshooting the hardware.'''
    # module 1
    for m in range(1, 4):
        for p in range(1, 17):
            print(m, p)
            switch_module_pin(m, p)


def hacktype(string_to_hacktype):
    print(len(string_to_hacktype))


if __name__ == "__main__":
    i2cbus = SMBus(1)  # i2cbus object creation
    initialize_I2Cs()
    while (True):
        switch_every_actuator_once()
        hacktype("yolo")