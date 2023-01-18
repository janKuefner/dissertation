class Robo_typer:
    def __init__(self, name):
        self.the_other_class = SMBus(name)

    def print_yolos(self):
        self.the_other_class.print_yolo("motherfucker")
        print("la la la")
        self.the_other_class.print_yolo("ding dong")


class SMBus:
    def __init__(self, name):
        self.name = name

    def print_yolo(self, var_1):
        print("yolo", var_1)


my_object = Robo_typer("bert")
my_object.print_yolos()
print(my_object.the_other_class.name)
