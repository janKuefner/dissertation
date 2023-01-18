from smbus2 import SMBus  # necessary for I2C communication
from time import sleep  # necessary for I2 communication


class Robo_typer(SMBus):
    def __init__(self):
        self.i2cbus = SMBus(1)

    def initialize_I2Cs(self):
        #  initializing I2C adress 0x20
        '''I2C address 0x20, side A, GPIOs set to output'''
        self.i2cbus.write_word_data(0x20, 0x00, 0x00)
        '''I2C address 0x20, side B, GPIOs set to output'''
        self.i2cbus.write_word_data(0x20, 0x01, 0x00)
        #  initializing I2C adress 0x21
        '''I2C address 0x20, side A, GPIOs set to output'''
        self.i2cbus.write_word_data(0x21, 0x00, 0x00)
        '''I2C address 0x20, side B, GPIOs set to output'''
        self.i2cbus.write_word_data(0x21, 0x01, 0x00)
        #  initializing I2C adress 0x22
        '''I2C address 0x20, side A, GPIOs set to output'''
        self.i2cbus.write_word_data(0x22, 0x00, 0x00)
        '''I2C address 0x20, side B, GPIOs set to output'''
        self.i2cbus.write_word_data(0x22, 0x01, 0x00)

    def switch_module_pin(self, module, pin):
        '''this funnction sitches actuator of a certain module and pin'''
        # general times the actuator stays actived / deactiveted
        time_actuator_on = 0.1   # time the actuator is powered.
        time_actuator_off = 0.01  # time the actuator is off.
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
                self.i2cbus.write_byte_data(i2caddress, A_or_B_side, pin_hex)
                sleep(time_actuator_on)
                sent = True
            except OSError:
                sent = False
        ''' switch off A and B side'''
        sent = False
        while (sent == False):
            try:
                self.i2cbus.write_byte_data(i2caddress, 0x12, 0x00)
                sleep(time_actuator_off / 2)
                sent = True
            except OSError:
                sent = False
        sent = False
        while (sent == False):
            try:
                self.i2cbus.write_byte_data(i2caddress, 0x15, 0x00)
                sleep(time_actuator_off / 2)
                sent = True
            except OSError:
                sent = False

    def switch_row_pin(self, row, pin):
        '''this function switches the pin per row of a keyboard'''
        if row == 1:
            if pin == 1:
                self.switch_module_pin(3, 3)
            elif pin == 2:
                self.switch_module_pin(1, 10)
            elif pin == 3:
                self.switch_module_pin(1, 11)
            elif pin == 4:
                self.switch_module_pin(1, 12)
            elif pin == 5:
                self.switch_module_pin(1, 14)
            elif pin == 6:
                self.switch_module_pin(1, 13)
            elif pin == 7:
                self.switch_module_pin(1, 15)
            else:
                raise ValueError("This pin number is not defined in this row")
        elif row == 2:
            if pin == 1:
                self.switch_module_pin(3, 2)
            elif pin == 2:
                self.switch_module_pin(2, 9)
            elif pin == 3:
                self.switch_module_pin(2, 10)
            elif pin == 4:
                self.switch_module_pin(2, 11)
            elif pin == 5:
                self.switch_module_pin(2, 12)
            elif pin == 6:
                self.switch_module_pin(2, 14)
            elif pin == 7:
                self.switch_module_pin(2, 13)
            elif pin == 8:
                self.switch_module_pin(2, 15)
            elif pin == 9:
                self.switch_module_pin(2, 16)
            elif pin == 10:
                self.switch_module_pin(3, 11)
            elif pin == 11:
                self.switch_module_pin(3, 9)
            else:
                raise ValueError("This pin number is not defined")
        elif row == 3:
            if pin == 1:
                self.switch_module_pin(3, 15)
            elif pin == 2:
                self.switch_module_pin(1, 4)
            elif pin == 3:
                self.switch_module_pin(1, 3)
            elif pin == 4:
                self.switch_module_pin(1, 2)
            elif pin == 5:
                self.switch_module_pin(1, 1)
            elif pin == 6:
                self.switch_module_pin(3, 10)
            elif pin == 7:
                self.switch_module_pin(3, 12)
            elif pin == 8:
                self.switch_module_pin(3, 5)
            elif pin == 9:
                self.switch_module_pin(3, 6)
            elif pin == 10:
                self.switch_module_pin(3, 13)
            elif pin == 11:
                self.switch_module_pin(3, 4)
            else:
                raise ValueError("This pin number is not defined")
        elif row == 4:
            if pin == 1:
                self.switch_module_pin(1, 7)
            elif pin == 2:
                self.switch_module_pin(1, 6)
            elif pin == 3:
                self.switch_module_pin(2, 8)
            elif pin == 4:
                self.switch_module_pin(1, 8)
            elif pin == 5:
                self.switch_module_pin(2, 6)
            elif pin == 6:
                self.switch_module_pin(2, 7)
            elif pin == 7:
                self.switch_module_pin(2, 4)
            elif pin == 8:
                self.switch_module_pin(2, 5)
            elif pin == 9:
                self.switch_module_pin(2, 2)
            elif pin == 10:
                self.switch_module_pin(2, 3)
            elif pin == 11:
                self.switch_module_pin(2, 1)
            else:
                raise ValueError("This pin number is not defined")
        else:
            raise ValueError("This row number is not defined")

    def switch_every_actuator_once(self):
        '''this function switches all actuators once. This function is sort of
        to help setting up or troubleshooting the hardware.'''
        for m in range(1, 4):
            for p in range(1, 17):
                self.switch_module_pin(m, p)

    def switch_every_actuator_once_sorted(self):
        '''this function switches all actuators once. This function is sort of
        to help setting up or troubleshooting the hardware.'''
        for p in range(1, 8):
            self.switch_row_pin(1, p)
            sleep(0.5)
            print("Reihe ", 1, " Pin ", p, "hat geschalten")

        for m in range(2, 5):
            for p in range(1, 12):
                self.switch_row_pin(m, p)
                sleep(0.5)
                print("Reihe ", m, " Pin ", p, "hat geschalten")

    def hack_type_char(self, char_to_hacktype):
        '''row 1'''
        if char_to_hacktype == " ":
            self.switch_row_pin(1, 4)
            ''' row 2 small letters '''
        elif char_to_hacktype == "z":
            self.switch_row_pin(2, 2)
        elif char_to_hacktype == "x":
            self.switch_row_pin(2, 3)
        elif char_to_hacktype == "c":
            self.switch_row_pin(2, 4)
        elif char_to_hacktype == "v":
            self.switch_row_pin(2, 5)
        elif char_to_hacktype == "b":
            self.switch_row_pin(2, 6)
        elif char_to_hacktype == "n":
            self.switch_row_pin(2, 7)
        elif char_to_hacktype == "m":
            self.switch_row_pin(2, 8)
            ''' row 3 small letters '''
        elif char_to_hacktype == "a":
            self.switch_row_pin(3, 2)
        elif char_to_hacktype == "s":
            self.switch_row_pin(3, 3)
        elif char_to_hacktype == "d":
            self.switch_row_pin(3, 4)
        elif char_to_hacktype == "f":
            self.switch_row_pin(3, 5)
        elif char_to_hacktype == "g":
            self.switch_row_pin(3, 6)
        elif char_to_hacktype == "h":
            self.switch_row_pin(3, 7)
        elif char_to_hacktype == "j":
            self.switch_row_pin(3, 8)
        elif char_to_hacktype == "k":
            self.switch_row_pin(3, 9)
        elif char_to_hacktype == "l":
            self.switch_row_pin(3, 10)
            ''' row 4 small letters '''
        elif char_to_hacktype == "q":
            self.switch_row_pin(4, 1)
        elif char_to_hacktype == "w":
            self.switch_row_pin(4, 2)
        elif char_to_hacktype == "e":
            self.switch_row_pin(4, 3)
        elif char_to_hacktype == "r":
            self.switch_row_pin(4, 4)
        elif char_to_hacktype == "t":
            self.switch_row_pin(4, 5)
        elif char_to_hacktype == "y":
            self.switch_row_pin(4, 6)
        elif char_to_hacktype == "u":
            self.switch_row_pin(4, 7)
        elif char_to_hacktype == "i":
            self.switch_row_pin(4, 8)
        elif char_to_hacktype == "o":
            self.switch_row_pin(4, 9)
        elif char_to_hacktype == "p":
            self.switch_row_pin(4, 10)
        else:
            # raise ValueError("This char is not defined")
            print(char_to_hacktype, " is not defined")

    def hack_type_string(self, string_to_hacktype):
        for letter in string_to_hacktype:
            self.hack_type_char(letter)
