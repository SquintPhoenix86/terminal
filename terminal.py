#Terminal
#This is the start of a 'prototype' terminal.


#libraries in use
import datetime
import math
import random
import string
import os


#programs
#this is the code correspoding to the calculator
def calc():
    exe = 1 
    while exe == 1:    
        print("Calculator")
        x = int(input("Please enter the number you want to use.\n"))
        print("""The operations that this calculator is capable of are:
        1. Multiplication
        2. Division
        3. Addition
        4. Subtraction
        5. Sine
        6. Cosine
        7. Factorial
        8. Square Root
        """)
        op = int(input("Please enter the number corresponding to the operation.\n"))
        if op < 0 or op > 8:
            print("Error: Invalid Number Entered")
        else:
            if op == 1:
                mult = int(input("Please enter the number you want to multiply to.\n"))
                result = x * mult
                print("The result of the operation is: ", result)
            elif op == 2:
                div = int(input("Please enter the number you want to divide to.\n"))
                result = x / div
                print("The result of the operation is: ", result)
            elif op == 3:
                sum = int(input("Please enter the number you want to add.\n"))
                result = x + sum
                print("The result of the operation is: ", result)
            elif op == 4:
                subt = int(input("Please enter the number you want to subtract.\n"))
                result = x - subt
                print("The result of the operation is: ", result)
            elif op == 5:
                result = math.sin(x)
                print("The result of the operation is: ", result)
            elif op == 6:
                result = math.cos(x)
                print("The result of the operation is: ", result)
            elif op == 7:
                result = math.factorial(x)
                print("The result of the operation is: ", result)
            elif op == 8:
                result = math.sqrt(x)
                print("The result of the operation is: ", result)
            exe = int(input("Do you want to run the program again? Press 1 if so.\n"))
    menu()
#this is the code corresponding to the password gen
def passgen():
    exe = 1
    while exe == 1:
        print("Password Generator v0.1")
        length = int(input("Enter the length of the password.\n"))
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all,length)
        password = "".join(temp)
        print("The generated password is: ", password)
        exe = int(input("Do you want to run the program again? Press 1 if so.\n"))
    menu()
#this is the code corresponding to rock-paper-scissors game
def rockpaperscissors():
    exe = "y"
    while exe == "y":
        user_input = input("""Please enter your choice:
        rock
        paper
        scissors\n""")
        possible_answers = ["rock","paper","scissors"]
        cpu_action = random.choice(possible_answers)
        print(f"You chose {user_input}, computer chose {cpu_action}.")
        if user_input == cpu_action:
            print(f"Both players chose {user_input}. It's a Tie!")
        elif user_input == "rock":
            if cpu_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_input == "paper":
            if cpu_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_input == "scissors":
            if cpu_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        exe = input("Play again? (y/n): ")
    menu()
#this is the code corresponding to madlibs
def madlibs():
    exe = 1
    while exe == 1:
        noun = input("Choose a noun: ")
        p_noun = input("Choose a plural noun: ")
        noun2 = input("Choose a noun: ")
        place = input("Name a place: ")
        adjective = input("Choose an adjective (Describing word): ")
        noun3 = input("Choose a noun: ")
        print ("------------------------------------------")
        print (f"Be kind to your {noun}-footed", p_noun)
        print (f"For a duck may be somebody's {noun2},")
        print ("Be kind to your",p_noun,"in",place)
        print (f"Where the weather is always {adjective}.")
        print ()
        print (f"You may think that is this the {noun3},")
        print ("Well it is.")
        print ("------------------------------------------")
        exe = int(input("Do you want to execute the program again? Press 1 if so."))
    menu()
#basic menu code
def menu():
    if os.name == "nt":
        os_name = "Windows NT Family - Vista, 7, 8, 10, 11"
    if os.name == "posix":
        os_name = "POSIX"
    if os.name == "os2":
        os_name = "OS/2"
    if os.name == "ce":
        os_name = "Windows Embedded Compact "
    now = datetime.datetime.now()
    print("Terminal v1.2")
    print("The operating system detected is: ", os_name)
    print("Current date and time at time of boot up: ")
    print(str(now))
    print("""Program List:
    1. Calculator
    2. Password Generator
    3. Rock, Paper, Scissors!
    4. Mad Libs Generator
    5. Exit
    """)
    program = int(input("Please enter the number corresponding to the program you want to execute.\n"))
    if program == 1:
        calc()
    elif program == 2:
        passgen()
    elif program == 3:
        rockpaperscissors()
    elif program == 4:
        madlibs()
menu()