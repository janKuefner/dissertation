import json


def switch_module_pin(a, b):
    print(a, b)


def switch_row_pin(row, pin):
    for x in range(8):
        if ((e_to_m_data[x]["row"]) == row and (e_to_m_data[x]["actuator"]) == pin):
            print("row", row, " actuator", pin)
            # print(data[x]["module"])
            # print(data[x]["outlet_number"])
            switch_module_pin((e_to_m_data[x]["module"]), (e_to_m_data[x]["outlet_number"]))


with open('electronics_to_mechanics.json') as json_file:
    e_to_m_data = json.load(json_file)
switch_row_pin(1, 3)
