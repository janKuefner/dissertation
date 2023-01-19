from smbus2 import SMBus  # necessary for I2C communication
from time import sleep  # necessary for I2 communication
import json


class Robo_typer(SMBus):
    def __init__(self):
        self.i2c = SMBus(1)
        self.switched_to_numbers = False

    def initialize_I2Cs(self):
        '''initializing all 3 I2C GPIO chips of the machine on both sides.
        1st value is the chip adress, 32 = chip 1, 33 = chip 2, ...
        2nd value is the side of the chip 0 = side A, 1 = side B
        3rd value is the command. 0 sets the GPIO pins to output
        I2C address 0x20, side A, GPIOs set to output'''
        self.i2c.write_word_data(32, 0, 0)
        self.i2c.write_word_data(32, 1, 0)
        self.i2c.write_word_data(33, 0, 0)
        self.i2c.write_word_data(33, 1, 0)
        self.i2c.write_word_data(34, 0, 0)
        self.i2c.write_word_data(34, 1, 0)

    def switch_module_outlet(self, module, outlet):
        '''this funnction sitches actuator of a certain module and
        outlet'''
        time_actuator_on = 0.1   # time the actuator is powered.
        time_actuator_off = 0.01  # time the actuator is off.
        with open('modules/I2C_data.json') as json_file:
            I2C_data = json.load(json_file)
        sent = False
        while (sent is False):
            try:
                for x in range(51):
                    if (((I2C_data[x]["module"] == module
                          and I2C_data[x]["outlet"] == outlet))):
                        elmnt_act = x
                self.i2c.write_byte_data(((I2C_data[elmnt_act]["module_I2C"])),
                                         ((I2C_data[elmnt_act]["side_I2C"])),
                                         ((I2C_data[elmnt_act]["outlet_I2C"])))
                sleep(time_actuator_on)
                sent = True
            except OSError:
                sent = False
        sent = False
        while (sent is False):
            try:
                self.i2c.write_byte_data(((I2C_data[elmnt_act]["module_I2C"])),
                                         ((I2C_data[elmnt_act]["side_I2C"])),
                                         (0))
                sleep(time_actuator_off)
                sent = True
            except OSError:
                sent = False

    def switch_row_actuator(self, row, actuator):
        with open('modules/electronics_to_mechanics.json') as json_file:
            e_to_m_data = json.load(json_file)
            data_entry_found = False
        for x in range(40):
            if (((e_to_m_data[x]["row"] == row and
                  e_to_m_data[x]["actuator"] == actuator))):
                self.switch_module_outlet((e_to_m_data[x]["module"]),
                                          (e_to_m_data[x]["outlet"]))
                data_entry_found = True
        if data_entry_found is False:
            raise ValueError("row #", row, "actuator #", actuator,
                             " combination is not defined")

    def switch_every_actuator_once(self):
        '''this function switches all actuators once. This function is sort of
        to help setting up or troubleshooting the hardware.'''
        for m in range(1, 4):
            for p in range(1, 17):
                self.switch_module_outlet(m, p)

    def switch_every_actuator_once_sorted(self):
        '''this function switches all actuators once. This function is
        to help setting up or troubleshooting the hardware.'''
        for p in range(1, 8):
            self.switch_row_actuator(1, p)
        for m in range(2, 5):
            for p in range(1, 12):
                self.switch_row_actuator(m, p)

    def type_char(self, char_to_hacktype):
        '''row 1'''
        if char_to_hacktype == " ":
            self.switch_row_actuator(1, 4)
            ''' row 2 '''
        elif char_to_hacktype == "z":
            self.switch_row_actuator(2, 2)
        elif char_to_hacktype == "x":
            self.switch_row_actuator(2, 3)
        elif char_to_hacktype == "c":
            self.switch_row_actuator(2, 4)
        elif char_to_hacktype == "v":
            self.switch_row_actuator(2, 5)
        elif char_to_hacktype == "b":
            self.switch_row_actuator(2, 6)
        elif char_to_hacktype == "n":
            self.switch_row_actuator(2, 7)
        elif char_to_hacktype == "m":
            self.switch_row_actuator(2, 8)
            ''' row 3  '''
        elif char_to_hacktype == "a":
            self.switch_row_actuator(3, 2)
        elif char_to_hacktype == "s":
            self.switch_row_actuator(3, 3)
        elif char_to_hacktype == "d":
            self.switch_row_actuator(3, 4)
        elif char_to_hacktype == "f":
            self.switch_row_actuator(3, 5)
        elif char_to_hacktype == "g":
            self.switch_row_actuator(3, 6)
        elif char_to_hacktype == "h":
            self.switch_row_actuator(3, 7)
        elif char_to_hacktype == "j":
            self.switch_row_actuator(3, 8)
        elif char_to_hacktype == "k":
            self.switch_row_actuator(3, 9)
        elif char_to_hacktype == "l":
            self.switch_row_actuator(3, 10)
            ''' row 4 '''
        elif char_to_hacktype == "q":
            self.switch_row_actuator(4, 1)
        elif char_to_hacktype == "w":
            self.switch_row_actuator(4, 2)
        elif char_to_hacktype == "e":
            self.switch_row_actuator(4, 3)
        elif char_to_hacktype == "r":
            self.switch_row_actuator(4, 4)
        elif char_to_hacktype == "t":
            self.switch_row_actuator(4, 5)
        elif char_to_hacktype == "y":
            self.switch_row_actuator(4, 6)
        elif char_to_hacktype == "u":
            self.switch_row_actuator(4, 7)
        elif char_to_hacktype == "i":
            self.switch_row_actuator(4, 8)
        elif char_to_hacktype == "o":
            self.switch_row_actuator(4, 9)
        elif char_to_hacktype == "p":
            self.switch_row_actuator(4, 10)
        else:
            # raise ValueError("This char is not defined")
            print(char_to_hacktype, " is not defined")

    def type_string(self, string_to_hacktype):
        for letter in string_to_hacktype:
            self.type_char(letter)
