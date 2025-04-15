# file for the interface of the program

import time
import os
from colorama import Fore, Style, Back, init
from defs import *

init(autoreset=True)

def main():
    while True:
        clear_screen()
        print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
        print("Welcome to the calculator program!")
        print("What would you like to do?\n")
        print("1. Basic operations")
        print("2. Formula operations")
        print("0. Exit")
        print("(Please enter the number of your choice)")
        
        try:
            choice = int(input("\nChoice: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")
            time.sleep(2)
            continue

        if choice not in [0, 1, 2]:
            print(Fore.RED + "Invalid choice. Please try again.")
            time.sleep(2)
            continue
        elif choice == 0:
            print(Fore.YELLOW + "Exiting the program...")
            time.sleep(2)
            clear_screen()
            break
        else:
            if choice == 1:
                clear_screen()
                print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                print("What would you like to do?\n")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Exponentiation")
                print("6. Square root")
                print("(Please enter the number of your choice)")
                
                try:
                    choice = int(input("\nChoice: "))
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid number.")
                    time.sleep(2)
                    continue

                if choice not in [1, 2, 3, 4, 5, 6]:
                    print(Fore.RED + "Invalid choice. Please try again.")
                    time.sleep(2)
                    continue
                else:
                    try:
                        if choice == 1:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the first number: "))
                            b = float(input("Please enter the second number: "))
                            result = sum(a, b)
                            print(Fore.YELLOW + f"The result of {a} + {b} is: {result}")
                            time.sleep(2)
                        elif choice == 2:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the first number: "))
                            b = float(input("Please enter the second number: "))
                            result = sub(a, b)
                            print(Fore.YELLOW + f"The result of {a} - {b} is: {result}")
                            time.sleep(2)
                        elif choice == 3:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the first number: "))
                            b = float(input("Please enter the second number: "))
                            result = mul(a, b)
                            print(Fore.YELLOW + f"The result of {a} * {b} is: {result}")
                            time.sleep(2)
                        elif choice == 4:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the first number: "))
                            b = float(input("Please enter the second number: "))
                            result = div(a, b)
                            if result == "e":
                                print(Fore.RED + "Error: Division by zero is not allowed.")
                                time.sleep(2)
                            else:
                                print(Fore.YELLOW + f"The result of {a} / {b} is: {result}")
                                time.sleep(2)
                        elif choice == 5:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the base number: "))
                            b = float(input("Please enter the exponent: "))
                            result = pow(a, b)
                            print(Fore.YELLOW + f"The result of {a} ^ {b} is: {result}")
                            time.sleep(2)
                        elif choice == 6:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the number: "))
                            result = sqrt(a)
                            if result == "e":
                                print(Fore.RED + "Error: Cannot calculate the square root of a negative number.")
                            else:
                                print(Fore.YELLOW + f"The square root of {a} is: {result}")
                            time.sleep(2)
                    except ValueError:
                        print(Fore.RED + "Invalid input. Please enter a valid number.")
                        time.sleep(2)
            
            elif choice == 2:
                clear_screen()
                print(Fore.YELLOW + "Formula operations are not implemented yet.")
                time.sleep(2)

if __name__ == "__main__":
    main()
