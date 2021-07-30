from parkinglot import Parking_Lot

class Menu:
    def menu(self):
        print()

        print("This program has been developed on the parking lot for the cars. It is easy to execute for anyone.")

        print()

        print("First of all, you have to create a parking lot of your required slots, to enjoy this app.")

        print()

        print("You can perform these following operations, to interact with this app.")

        print()

    def operations(self):
        print("To create parking lot, press :- 1")
        print("To park your car, press :- 2")
        print("To leave your car occupied slot, press :- 3")
        print("To know the status of the parking lot press :- 4")
        print("To get the registration numbers of particular color press :- 5")
        print("To get the slot numbers of particular color, press :- 6")
        print("To get the slot number of particular registration number, press :- 7")
        print("To go exit, press :- 0")

    def operations_Handler(self):
        parkingLot = Parking_Lot()

        while True:

            print("\n")

            userInput = input("Enter your choice: ")

            if userInput == "1":

                user_input_capacity_for_slots = input("Enter the slot capacity of parking lot: ")

                parkingLot.execute_lines("create_parking_lot {0}".format(user_input_capacity_for_slots))

            elif userInput == "2":

                print()

                user_reg_num = input("Enter registration number of the car: ")

                print()

                user_car_color = input("Enter the color of the car: ")

                print()

                parkingLot.execute_lines("park {0} {1}".format(user_reg_num,user_car_color))

            elif userInput == "3":

                print()

                slot_num_to_leave = input("Enter slot number to leave: ")

                print()

                parkingLot.execute_lines("leave {0}".format(slot_num_to_leave))
            
            elif userInput == "4":

                print()

                parkingLot.execute_lines("status")

            elif userInput == "5":

                print()

                color_to_get_reg_nums = input("Enter the particular color of car to get the registration numbers of cars, having same color: ")

                print()

                parkingLot.execute_lines("registration_numbers_for_cars_with_colour {0}".format(color_to_get_reg_nums))

            elif userInput == "6":

                print()

                color_to_get_slot_nums = input("Enter the particular color of car to get the slot numbers of cars, having same color: ")

                print()

                parkingLot.execute_lines("slot_numbers_for_cars_with_colour {0}".format(color_to_get_slot_nums))

            elif userInput == "7":

                print()

                reg_num_to_get_slot_num = input("Enter the registration number to get the slot number: ")

                print()

                parkingLot.execute_lines("slot_number_for_registration_number {0}".format(reg_num_to_get_slot_num))

            elif userInput == "0":

                print()

                print("Thank you!")

                print()

                parkingLot.execute_lines("exit")



    
