# CSC 4110 Assignment 5

import math                     # Math library for the square root function
from datetime import datetime   # datetime function for the month and date

first_Name = "derek"            # This variable stores my first name

last_Name = "RUGGIRELLO"        # This variable stores my last name

print("Hello,", first_Name.upper(), last_Name.lower())  # Print name using string functions

print("\n")                     # Creating a two line separation

full_Name = first_Name + " " + last_Name    # Creates variable with both first and last name

print(full_Name[6:16])          # Outputs just the last name in the full name variable

print("\n")                     # Creating a two line separation

print(full_Name.replace("RUGGIRELLO", "RUGGIRELLO, WALSH COLLEGE STUDENT\n"))   # Replacing last name with new string

print('''"Start by doing what\'s necessary; then do what\'s
possible; and suddenly you are doing the impossible
-Francis of Assisi"\n''')       # This output uses triple quotes in order to format the output correctly

decimal_Number = 1.8            # Stores one decimal number

second_Decimal = 9.2            # Stores second decimal number

decimal_Addition = decimal_Number + second_Decimal      # Stores decimal addition

decimal_Subtraction = decimal_Number - second_Decimal   # Stores decimal subtraction

decimal_Multiplication = decimal_Number * second_Decimal    # Stores decimal multiplication

decimal_Division = decimal_Number / second_Decimal      # Stores decimal division

print(decimal_Number, "plus", second_Decimal, "equals", decimal_Addition, "\n") # Outputs the decimals added together

print("{0} minus {1} equals {2}\n".format(decimal_Number, second_Decimal, decimal_Subtraction)) # Output using .format() function

print(f'{decimal_Number} multiplied by {second_Decimal} equals {decimal_Multiplication} \n')    # Output using f-string

print(str(decimal_Number) + " divided by " + str(second_Decimal) + " equals " + str(decimal_Division) + "\n")   # Output using concatenation

sq_root = math.sqrt(decimal_Multiplication)     # Variable to store square root equation

print("The square root of {} equals {:.2f}".format(decimal_Multiplication, sq_root))    # Uses formating to output square root

current_Month = datetime.now()     # Stores the current date

current_Month = current_Month.strftime("%B")    # Formats string for just the month

current_Day = int(datetime.now().day)           # Stores the current day in an integer variable

print(f"""      Today is day {current_Day} of the month of {current_Month}.""")     # Outputs using formatting for double tabs at the beginning