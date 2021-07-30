class Ticket:
    def __init__(self,reg_num,color):
        self.reg_num = reg_num
        self.color = color

class Car(Ticket):
    def __init__(self,reg_num,color):
        Ticket.__init__(self,reg_num,color)
        