class SMBus:
    def __init__(self, name):
        self.name = name

    def write_word_data(self, var_1, var_2, var_3):
        print(var_1, var_2, var_3, "yolo")


class Robo_typer(SMBus):
    pass

    def initalize(self):
        print("yolo")

    def print_mf(self):
        print("MF")


my_object = Robo_typer("bert")
my_object.write_word_data(1, "bla", 3)
my_object.print_mf()
print(my_object.name)
