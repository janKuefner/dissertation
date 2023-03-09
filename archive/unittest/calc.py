import json


class Yolo():
    def __init__(self):
        self.set_2_spcl = False

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
                # self.switch_module_outlet((e_to_m_data[x]["module"]),
                #                             (e_to_m_data[x]["outlet"]))
                data_entry_found = True
                return ("yolo")
        if data_entry_found is False:
            raise ValueError("row #", row, "actuator #", actuator, " combination is not defined")

# def yolo():
#    print(yolo2.write_byte_data(32, 0, 0))


# yolo2 = SMBus(1)
# yolo()
