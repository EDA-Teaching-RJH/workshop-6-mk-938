#Your code goes here. 

import math

def safe_divide(a, b):
    try:
        return (a/b)
    except ZeroDivisionError:
        return ("Can't divide by 0")
        

def process_list(input_list):
    total = 0
    for item in input_list:
        try:
            total+=item**2
        except (TypeError, ValueError):
            continue
    return total

def nested_operations(a, b):
    try:
        a = int(a)
        b = int(b)
        try:
            c = a/b
            return c**0.5
        except ZeroDivisionError:
            return ("Can't divide by zero")
    except ValueError:
        return ("not int")

def process_input():
    number = input("Please enter a number: ")
    try:
        num = float(number)
    except ValueError:
        print ("That was not an integer")
    else:
        print (num**2)
    finally:
        print("Processing complete")

    

def main():
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(process_list([1, '2', 3, 'four', 5]))    
    print(nested_operations(16, 4))
    print(nested_operations(10, 0))
    print(nested_operations('a', 5))
    process_input()

main()
