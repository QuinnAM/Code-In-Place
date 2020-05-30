
import random

WEIGHT_DICT = {"sugar glider" : 0.12,
               "hedgehog" : 0.8,
               "teaspoon" : 0.02,
               "lego minifig" : 0.0029
               }


def main():


    orig_weight = float(input("Please enter your start weight: "))
    new_weight = float(input("Please enter your current weight: "))
    lost_weight = (orig_weight - new_weight)

    random_unit = choose_random_unit()
    unit_weight = lost_weight / random_unit[1]

    print_congratulations_message(lost_weight)
    print_weight_in_units(unit_weight, random_unit)

def choose_random_unit():
    random_unit = random.choice(list(WEIGHT_DICT.items()))
    return random_unit


def print_congratulations_message(lost_weight):

    if lost_weight == 1:
        print ("Congratulations! You have lost " + str(int(lost_weight)) + " kilo!")
    elif (lost_weight % 1 != 0):
        print("Congratulations! You have lost " + str(lost_weight) + " kilos!")
    elif (lost_weight % 1 == 0):
        print("Congratulations! You have lost " + str(int(lost_weight)) + " kilos!")


def print_weight_in_units(unit_weight, random_unit):

    if unit_weight == 1:
        print ("That is " + str(int(unit_weight)) + " " + random_unit[0] + "!")
    elif (unit_weight % 1 != 0):
        print("That is " + str(unit_weight) + " " + random_unit[0] +"s!")
    elif (unit_weight % 1 == 0):
        print("That is " + str(int(unit_weight)) + " " + random_unit[0] + "s!")

if __name__ == '__main__':
    main()