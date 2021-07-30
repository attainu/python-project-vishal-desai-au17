from parkinglot import Parking_Lot
from menu import Menu

if __name__ == "__main__":

    parkingLot = Parking_Lot()

    menuDriven = Menu()

    print()

    print(" Press 1 for file driven inputs\n Press 2 for menu driven inputs\n Press 3 for user driven inputs")

    print()

    user_input_direction_to_run = input("Enter your choice: ")

    if user_input_direction_to_run == "1":

        myFile = open('commands.txt')

        for command in myFile:
            parkingLot.execute_lines(command)
        print()

    elif user_input_direction_to_run == "2":

        menuDriven.menu()

        menuDriven.operations()

        menuDriven.operations_Handler()

    elif user_input_direction_to_run == "3":
        print("To go exit, type exit")
        while True:
            print()
            command = input("$")
            parkingLot.execute_lines(command)



