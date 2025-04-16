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
                print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                print("What would you like to do?\n")
                print("1. Area of a circle")
                print("2. Area of a square")
                print("3. Area of a rectangle")
                print("4. Area of a triangle")
                print("5. Quadratic formula")
                print("6. Pythagorean theorem")
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
                            radius = float(input("Please enter the radius of the circle: "))
                            result = area_circle(radius)
                            print(Fore.YELLOW + f"The area of the circle with radius {radius} is: {result}")
                            time.sleep(2)
                        elif choice == 2:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            side = float(input("Please enter the side length of the square: "))
                            result = area_square(side)
                            print(Fore.YELLOW + f"The area of the square with side length {side} is: {result}")
                            time.sleep(2)
                        elif choice == 3:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            length = float(input("Please enter the length of the rectangle: "))
                            width = float(input("Please enter the width of the rectangle: "))
                            result = area_rectangle(length, width)
                            print(Fore.YELLOW + f"The area of the rectangle with length {length} and width {width} is: {result}")
                            time.sleep(2)
                        elif choice == 4:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            base = float(input("Please enter the base of the triangle: "))
                            height = float(input("Please enter the height of the triangle: "))
                            result = area_triangle(base, height)
                            print(Fore.YELLOW + f"The area of the triangle with base {base} and height {height} is: {result}")
                            time.sleep(2)
                        elif choice == 5:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter coefficient a: "))
                            b = float(input("Please enter coefficient b: "))
                            c = float(input("Please enter coefficient c: "))
                            
                            result = quadratic_formula(a, b, c)
                            if result == "e":
                                print(Fore.RED + "Error: No real roots exist.")
                            else:
                                x1, x2 = result
                                print(Fore.YELLOW + f"The roots of the equation are: x1 = {x1}, x2 = {x2}")
                                time.sleep(2)
                        elif choice == 6:
                            clear_screen()
                            print(Fore.GREEN + "\n- - - C A L C U L A T O R - - -\n")
                            a = float(input("Please enter the length of side a: "))
                            b = float(input("Please enter the length of side b: "))
                            result = pitagorean_theorem(a, b)
                            print(Fore.YELLOW + f"The length of the hypotenuse is: {result}")
                            time.sleep(2)
                    except ValueError:
                        print(Fore.RED + "Invalid input. Please enter a valid number.")
                        time.sleep(2)

if __name__ == "__main__":
    main()
