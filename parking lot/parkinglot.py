import ticket


class Parking_Lot:

    def __init__(self):

        self.capacity = 0

        self.slot_number = 0

        self.num_of_engaged_slots = 0


    def create_parking_lot(self,capacity):

        self.slots = [-1] * capacity

        self.capacity = capacity

        return self.capacity


    def get_available_slot(self):

        for i in range(len(self.slots)):

            if self.slots[slot] == -1:

                return i
    

    def park(self,reg_num, color):

        if self.num_of_engaged_slots < self.capacity:

            slot_number = self.get_available_slot()

            self.slots[slot_number] = ticket.Car(reg_num,color)

            self.slot_number = self.slot_number + 1

            self.num_of_engaged_slots = self.num_of_engaged_slots + 1

            return slot_number + 1

        else:

            return -1


    def leave(self,slot_number):

        if self.num_of_engaged_slots > 0 and self.slots[slot_number-1] != -1:

            self.slots[slot_number - 1] = -1

            self.num_of_engaged_slots = self.num_of_engaged_slots - 1

            return True
        
        else:

            return False


    def status(self):

        print("Slot No.",end="  ")

        print("Registration No.", end="  ")

        print("Color")

        print()

        for slot in range(len(self.slots)):

            if self.slots[slot] == -1:

                print(str(slot + 1), end="         ")

                print("--Empty--", end="         ")

                print("--Empty--",end="  ")

                print()

            else:

                print(str(slot + 1), end="         ")

                print(self.slots[slot].reg_num, end="     ")

                print(self.slots[slot].color,end="  ")

                print()


    def get_reg_nums_from_color(self,color):

        reg_nos = list()

        for slot in self.slots:

            if slot == -1:

                continue

            if slot.color == color:

                reg_nos.append(slot.reg_num)

        return reg_nos


    def get_slot_nums_from_color(self,color):

        slot_nums = list()

        for slot in range(len(self.slots)):

            if self.slots[slot] == -1:
                
                continue

            if self.slots[slot].color == color:

                slot_nums.append(str(slot + 1))

        return slot_nums


    def get_slot_num_from_reg_num(self,reg_num):

        for slot in range(len(self.slots)):

            if self.slots[slot].reg_num == reg_num:

                return slot + 1

            else:

                continue
        return "Not Found"

    def execute_lines(self,line):

        lines = line.split(' ')


        if lines[0] == "create_parking_lot":

            capacity = int(lines[1])

            parkingLotCreated = self.create_parking_lot(capacity)

            print("Created a parking lot with",parkingLotCreated,"slots")


        elif lines[0] == "park":

            regNum = lines[1]

            color = lines[2]

            slot_num_to_park = self.park(regNum,color)

            if slot_num_to_park == -1:

                print("Sorry, parking lot is full.")

            else:

                print("Allocated slot number:",slot_num_to_park)
                

        elif lines[0] == "leave":

            slotNum = int(lines[1])

            leaving_slot_num = self.leave(slotNum)

            if leaving_slot_num:

                print("Slot number " + str(slotNum) + " is free")
            else:

                print("No car is there in the parking lot!")

        elif lines[0] == "status":

            self.status()

        
        elif lines[0] == "registration_numbers_for_cars_with_colour":

            color = lines[1]

            reg_num_of_cars = self.get_reg_nums_from_color(color)

            print(', '.join(reg_num_of_cars))

        
        elif lines[0] == "slot_numbers_for_cars_with_colour":

            color = lines[1]

            slot_nums_for_cars = self.get_slot_nums_from_color(color)

            print(', '.join(slot_nums_for_cars))


        elif lines[0] == "slot_number_for_registration_number":

            regd_num = lines[1]

            slot_num_of_car = self.get_slot_num_from_reg_num(regd_num)

            print(str(slot_num_of_car))
        

        elif lines[0] == "exit":

            exit(0)




