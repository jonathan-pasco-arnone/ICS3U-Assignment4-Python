#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines the cost of a person's order and whether
# they get a discount


def main():
    # This function determines the cost of a person's order and whether
    # they get a discount

    print("")
    print("This program calculates the cost of your order!")
    print("")
    quantity_str = input("Please enter the number of items you"
                         " are purchasing: ")
    print("")

    try:
        quantity = int(quantity_str)
    except Exception:
        print("Invalid Input")
    else:
        if quantity > 0:
            subtotal = quantity * 100
            if subtotal >= 999:
                total = subtotal * 0.9 * 1.13
            else:
                total = subtotal * 1.13
            print("Your subtotal is ${:.2f}\nYour total"
                  " is ${:.2f}".format(subtotal, total))
        elif quantity == 0:
            print("If you have not purchased anything than you"
                  " have no reason to use this program")
        else:
            print("Please put in an actual quantity")


if __name__ == "__main__":
    main()
