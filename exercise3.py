#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("The battery cables may be damaged. Replace cables and try again.")


diagnose_car()
#question and text box that requires users to input the answer
#question 1
diagnose_car1 = raw_input('Is the car silent when you turn the key? (Yes/No):')

#yes to question 1, display question 2
if diagnose_car == "yes":
    diagnose_car = raw_input('Are the battery terminals corroded? (Yes/No):')
#yes to question 2
    if diagnose_car == "yes":
        print('Clean terminals and start again.')
#
    elif diagnose_car == "no":
        print('Replace cables and try again.')

elif diagnose_car == "no":
    diagnose_car = raw_input('Does the car make a clicking noise? (Yes/No):')

    if diagnose_car == "yes":
        print('Replace the battery')
    elif diagnose_car == "no":
        diagnose_car = raw_input('Does the car crank up but fail to start? (Yes/No):')

    if diagnose_car == "yes":
        print('Check spark plug connections.')
    elif diagnose_car == "no":
        diagnose_car = raw_input('Does the engine start and then die? (Yes/No):')

        if diagnose_car == "yes":
            diagnose_car = raw_input('Does your car have fuel injection? (Yes/No):')

            if diagnose_car == "yes":
                print('Check to ensure the choke is opening and closing.')
            elif diagnose_car == "no":
                print('Get it in for service.')

        elif diagnose_car == "no":
            print('Engine is not getting enough fuel. Clean fuel pump.')

