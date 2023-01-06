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
    '''this funnction sitches actuator of a certain module and pin'''
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
        raise ValueError("This module number is not defined")
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


def switch_row_pin(row, pin):
    '''this function switches the pin per row of a keyboard'''
    if row == 1:
        if pin == 1:
            print("yolo")
        elif pin == 2:
            switch_module_pin(1, 10)
        elif pin == 3:
            switch_module_pin(1, 11)
        elif pin == 4:
            switch_module_pin(1, 12)
        elif pin == 5:
            switch_module_pin(1, 14)
        elif pin == 6:
            switch_module_pin(1, 13)
        elif pin == 7:
            switch_module_pin(1, 15)
        else:
            raise ValueError("This pin number is not defined in this row")
    elif row == 2:
        if pin == 1:
            print("yolo")
        elif pin == 2:
            switch_module_pin(2, 9)
        elif pin == 3:
            switch_module_pin(2, 10)
        elif pin == 4:
            switch_module_pin(2, 11)
        elif pin == 5:
            switch_module_pin(2, 12)
        elif pin == 6:
            switch_module_pin(2, 14)
        elif pin == 7:
            switch_module_pin(2, 13)
        elif pin == 8:
            switch_module_pin(2, 15)
        elif pin == 9:
            switch_module_pin(2, 16)
        elif pin == 10:
            switch_module_pin(3, 2)
        elif pin == 11:
            switch_module_pin(3, 1)
        else:
            raise ValueError("This pin number is not defined")
    elif row == 3:
        if pin == 1:
            print("yolo")
        elif pin == 2:
            switch_module_pin(1, 4)
        elif pin == 3:
            switch_module_pin(1, 3)
        elif pin == 4:
            switch_module_pin(1, 2)
        elif pin == 5:
            switch_module_pin(1, 1)
        elif pin == 6:
            print("yolo")
        elif pin == 7:
            switch_module_pin(3, 8)
        elif pin == 8:
            switch_module_pin(3, 5)
        elif pin == 9:
            switch_module_pin(3, 6)
        elif pin == 10:
            switch_module_pin(3, 3)
        elif pin == 11:
            switch_module_pin(3, 4)
        else:
            raise ValueError("This pin number is not defined")
    elif row == 4:
        if pin == 1:
            switch_module_pin(1, 7)
        elif pin == 2:
            switch_module_pin(1, 6)
        elif pin == 3:
            switch_module_pin(2, 8)
        elif pin == 4:
            switch_module_pin(1, 8)
        elif pin == 5:
            switch_module_pin(2, 6)
        elif pin == 6:
            switch_module_pin(2, 7)
        elif pin == 7:
            switch_module_pin(2, 4)
        elif pin == 8:
            switch_module_pin(2, 5)
        elif pin == 9:
            switch_module_pin(2, 2)
        elif pin == 10:
            switch_module_pin(2, 3)
        elif pin == 11:
            switch_module_pin(2, 1)
        else:
            raise ValueError("This pin number is not defined")
    else:
        raise ValueError("This row number is not defined")


def switch_every_actuator_once():
    '''this function switches all actuators once. This function is sort of to
    help setting up or troubleshooting the hardware.'''
    for m in range(1, 4):
        for p in range(1, 17):
            switch_module_pin(m, p)


def switch_every_actuator_once_sorted():
    '''this function switches all actuators once. This function is sort of to
    help setting up or troubleshooting the hardware.'''
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    for p in range (1,8):
        switch_row_pin(1, p)
        time.sleep(1)
        print("Reihe ", 1, " Pin ", p, "hat geschalten")

    for m in range(2, 5):
        for p in range(1, 12):
            switch_row_pin(m, p)
            time.sleep(1)
            print("Reihe ", m, " Pin ", p, "hat geschalten")


def hack_type_char(char_to_hacktype):
    if char_to_hacktype == "a":
        switch_module_pin(1, 1)
    elif char_to_hacktype == "b":
        switch_module_pin(1, 2)
    else:
        # raise ValueError("This char is not defined")
        print("This char is not defined")


if __name__ == "__main__":
    i2cbus = SMBus(1)  # i2cbus object creation
    initialize_I2Cs()
    # switch_row_pin(3, 5)
    # switch_every_actuator_once()
    switch_every_actuator_once()
    '''
    while (True):
        switch_every_actuator_once_sorted()
        # letter_to_type = input("Enter Char:")
        # hack_type_char(letter_to_type)
    '''
