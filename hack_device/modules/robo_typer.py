from smbus2 import SMBus  # smbus2 is necessary for I2C communication
from time import sleep  # sleep is used to pause the programm
import json  # json is used to read external Json files


class Robo_typer(SMBus):
    '''this object controls the typing hardware.'''
    def __init__(self):
        self.i2c = SMBus(1)  # Robo_typer inherits from SMBus Object
        self.set_2_spcl = False  # is the keyboard set to special characters

    def initialize_I2Cs(self):
        '''this method initializes all three I2C GPIO modules on both sides.
        1st value is the chip adress, 32 = chip 1, 33 = chip 2, 34 = chip 3
        2nd value is the side of the chip 0 = side A, 1 = side B
        3rd value is the command. 0 sets the GPIO pins to output'''
        self.i2c.write_word_data(32, 0, 0)
        self.i2c.write_word_data(32, 1, 0)
        self.i2c.write_word_data(33, 0, 0)
        self.i2c.write_word_data(33, 1, 0)
        self.i2c.write_word_data(34, 0, 0)
        self.i2c.write_word_data(34, 1, 0)

    def switch_module_outlet(self, module, outlet):
        '''this method switches the outlets on the three modules for a defined
        time active. By switching a certain outlet active the actuator can move
        and so the machine types. By deactivating the certain outlet again, the
        actuator will depowerize and retract to its inital position.
        The method takes module and outlet as arguments in order to switch this
        chosen module`s outlet.'''
        time_actuator_on = 0.1   # time the actuator is powered.
        time_actuator_off = 0.01  # time the actuator is off.
        '''the I2C GPIO modules need specific commands and parameters to switch
        properly. Since the commands are a lot and since it is easier to see
        the commands in a json file rather than in Phyton code, those commands
        were moved to a json file, which is now loaded.
        '''
        with open('modules/I2C_data.json') as json_file:  # open file
            I2C_data = json.load(json_file)  # parse json data
        sent = False  # this variable shows success of sending to a module
        while (sent is False):  # loop this sending is successfull
            try:
                for x in range(51):  # go through data structures in I2Cdata
                    if (((I2C_data[x]["module"] == module
                          and I2C_data[x]["outlet"] == outlet))):
                        elmnt_act = x  # when there is match store the number
                self.i2c.write_byte_data(((I2C_data[elmnt_act]["module_I2C"])),
                                         ((I2C_data[elmnt_act]["side_I2C"])),
                                         ((I2C_data[elmnt_act]["outlet_I2C"])))
                # write_byte_data throws an exception, if I2C does not work
                sleep(time_actuator_on)  # keeps actuator extended for a time
                sent = True  # only if there is no exception
            except OSError:
                sent = False  # in case of exception, keep looping.
        '''in the following the identical actions are done, except that the
        outlet ist actively set to 0 in order to deactivate the outlet again.
        '''
        sent = False
        while (sent is False):
            try:
                self.i2c.write_byte_data(((I2C_data[elmnt_act]["module_I2C"])),
                                         ((I2C_data[elmnt_act]["side_I2C"])),
                                         (0))  # deactivating the outlet
                sleep(time_actuator_off)  # keeps actuator off for a time
                sent = True
            except OSError:
                sent = False

    def add(self, x, y):
        """Add Function"""
        return x + y

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
        '''this method switches all actuators once. This method is sort of
        to help setting up or troubleshooting the hardware.'''
        for m in range(1, 4):
            for p in range(1, 17):
                self.switch_module_outlet(m, p)

    def switch_every_actuator_once_sorted(self):
        '''this method switches all actuators once. This method is
        to help setting up or troubleshooting the hardware.'''
        for p in range(1, 8):
            self.switch_row_actuator(1, p)
        for m in range(2, 5):
            for p in range(1, 12):
                self.switch_row_actuator(m, p)

    def type_char(self, char_to_type):
        with open('modules/char_to_mechanics.json') as json_file:
            c_to_m_data = json.load(json_file)
            data_entry_found = False
        for x in range(83):
            if (c_to_m_data[x]["char"] == char_to_type):
                if c_to_m_data[x]["special_state"] == "UP":
                    self.switch_row_actuator(2, 1)  # press SHIFT button
                if (((self.set_2_spcl is False and
                      c_to_m_data[x]["special_state"] == "Y"))):
                    self.switch_row_actuator(1, 1)  # switch to letters
                    self.set_2_spcl = True
                elif (self.set_2_spcl is True and
                      c_to_m_data[x]["special_state"] == "N"):
                    self.switch_row_actuator(1, 1)  # switch to numbers
                    self.set_2_spcl = False
                self.switch_row_actuator((c_to_m_data[x]["row"]),
                                         (c_to_m_data[x]["actuator"]))
                data_entry_found = True
        if data_entry_found is False:
            print(char_to_type, " is not defined")

    def type_string(self, string_to_type):
        for letter in string_to_type.strip():  # strip() deletes whitespaces
            self.type_char(letter)
