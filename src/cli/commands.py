from src.robot import Robot
from src.garage import Garage


# Commands that will be used by the users
class Commands:
    @staticmethod
    def start():
        # Starting screen, with a set of instructions to run
        print()
        print("####  OOP Project Assignment Interface  ####")
        print()
        print("Command list")
        print("1 -> Create a garage")
        print("2 -> Create a robot")
        print("3 -> Create procedure")
        print("4 -> Perform a action")
        print("5 -> Apply procedure")
        print("6 -> Show history")
        print("7 -> Show robot info")
        print("8 -> Sell a robot")
        print("9 -> List robots in the garage")
        print("0 -> Exit the program")

    @staticmethod
    def create_robot():
        print("-> Create a robot")
        print("   ##############")

        name = input("Robot name: ")

        try:
            energy = int(input("Robot energy (range 0-100): "))
            while 0 > energy or energy > 100:
                print(
                    "-> ERROR: Energy has to be more than 0 and less than 100"
                )
                energy = int(input("Robot energy (range 0-100): "))
        except ValueError:
            print("-> ERROR: Invalid energy value")
            return None

        try:
            happiness = int(input("Robot happiness (range 0-50): "))
            while 0 > happiness or happiness > 50:
                print(
                    "-> ERROR: Happiness has to be more than 0 and less "
                    "than 50"
                )
                happiness = int(input("Robot happiness (range 0-50): "))
        except ValueError:
            print("-> ERROR: Invalid happiness value")
            return None

        try:
            procedure = int(input("Robot procedure time (in milliseconds): "))
            while procedure < 0:
                print("-> ERROR: Procedure time has to be more than 0")
                procedure = int(
                    input("Robot procedure time (in milliseconds): ")
                )
        except ValueError:
            print("-> ERROR: Invalid procedure time")
            return None

        owner = input("Robot owner: ")

        return Robot(name, energy, happiness, procedure, owner)

    @staticmethod
    def create_garage():
        print("-> Create a garage")
        print("   ###############")

        try:
            capacity = int(input("Garage capacity: "))
            while capacity < 0:
                print(
                    "-> ERROR: The capacity of the garage has to be more "
                    "than 0"
                )
                capacity = int(input("Garage capacity: "))
        except ValueError:
            print("-> ERROR: Invalid capacity value")
            return None

        return Garage(capacity)

    @staticmethod
    def list_robots():
        print("-> Robots in the garage")
        print("   ####################")
        return True

    @staticmethod
    def sell_robot():
        print("-> Sale a robot")
        print("   ############")

        name = input("Robot name: ")
        owner = input("Owner: ")
        buyer = input("Buyer: ")
        return [name, owner, buyer]

    @staticmethod
    def perform_action():
        valid_actions = ["move", "talk", "work", "hibernate"]
        print("-> Perform a action")
        print("   ################")

        name = input("Robot name: ")
        owner = input("Robot owner: ")
        action = input("Action [move, talk, work, hibernate]: ").lower()

        while action not in valid_actions:
            print("Action is not allowed, try again")
            action = input("Action [move, talk, work, hibernate]: ").lower()

        return [name, owner, action]

    def create_procedure():
        print("-> Create procedure")
        print("   ################")
        proc_robots = []

        try:
            proc_time = int(input("Procedure time (in miliseconds): "))
            while proc_time < 0:
                print("-> ERROR: Procedure time has to be more than 0")
                proc_time = int(input("Procedure time (in miliseconds): "))
        except ValueError:
            print("-> ERROR: Procedure time value is not allowed")
            return None

        user_input = input("Add robot to procedure (y/n): ")
        while user_input != "n":
            bot_name = input("Robot name: ")
            bot_owner = input("Robot owner: ")
            proc_robots.append([bot_name, bot_owner])
            user_input = input("Add robot to procedure (y/n): ")

        return {
            "proc_time": proc_time,
            "robots": proc_robots
        }

    def apply_procedure():
        print("-> Apply procedure(s)")
        print("   ##################")

        res = input("What to see the procedures list (y/n)?: ").lower()
        while res not in ["y", "n"]:
            print("Yes (y) or No (n) anwer")
            res = input("Want to see the procedures list (y/n)?: ").lower()
        return True if res == "y" else False

    @staticmethod
    def show_history():
        print("-> History of actions")
        print("   ##################")
        return True

    @staticmethod
    def show_robot_info():
        print("-> Robot information")
        print("   #################")

        name = input("Robot name: ")
        owner = input("Robot owner: ")

        print("*************")
        return [name, owner]

    @staticmethod
    def exit():
        # Exit program
        print("Thanks for using me, have a good day")
