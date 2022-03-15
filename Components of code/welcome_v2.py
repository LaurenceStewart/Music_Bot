import random
from random import randint

#list of random names
names = ["Laurence", "George", "Toby", "Caleb", "Matthew", "Josh", "Terry", "Zach", "Luke", "Oscar"]
def welcome():
    '''
    Purpose: to generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    num = randint(0,9)
    name = (names[num])
    print("#### Welcome to Groovey Music ####")
    print("#### My name is",name, "####")
    print("#### I am here to help you order music albums of your choice ####")


def main():
    '''
    Purpose: To run all functions
    Parameters: none
    Returns: none
    '''
    welcome()

main()