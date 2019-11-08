"""
This code is a Choose Your Own Adventure Game
Author: Robyn Murray
"""
#import time for loading periods
from time import sleep

#function to check for correct input
def check_input(ans):
    if ans[0] == "1" or ans[0] == "2":
        print("Continuing....")
        sleep(2)
        return True
    else:
        print("Please indicate your choice by entering 1 or 2")
        return False

#get player choice
def choice():
    ans = input(">> ")
    p_status = check_input(ans)
    while not p_status:
        ans = input(">> ")
        p_status = check_input(ans)
    return ans

def first_scene():
    #first scene
    print("You are walking in the forest, when you come upon a stone house.")
    print("Do you Keep Walking (1) or Enter the House (2)? ")
    ans = choice()
    if ans[0] == "1":
        print("You chose to Keep Walking...")
        sleep(2)
        print("On the Other Side of the House a BEAR pops out and EATS YOU.")
        return False
    else:
        print("You chose to Enter the House...")
        sleep(2)
        return True

def second_scene():
    #second scene in house
    print("Inside the house you see a BLUE Door and a GREEN Door.")
    print("Do you enter the BLUE Door (1) or the GREEN Door (2)?")
    ans = choice()
    if ans[0] == "1":
        print("You chose the BLUE Door...")
        sleep(2)
        return "BLUE"
    else:
        print("You chose the GREEN Door...")
        sleep(2)
        return "GREEN"

def third_scene():
    #third scene
    print("You see a ladder stretching into an opening in the ceiling.")
    print("Do you Go Up the Ladder (1) or Go Back (2)?")
    ans = choice()
    if ans[0] == "1":
        print("You Go Up the Ladder...")
        sleep(2)
        print("At the top of the Ladder is a Dragon who BURNS YOU ALIVE.")
        sleep(2)
        print("YOU HAVE DIED :-X")
        #loop flag is now false and ends game
        return False
    else:
        print("You chose to Go Back...")
        sleep(2)
        #loop again through second scene
        return True

def fourth_scene():
    #fourth scene
    print("You see a staircase that winds down.")
    print("Do you Go Down the Staircase (1) or Go Back (2)?")
    ans = choice()
    if ans[0] == "1":
        print("You Go Down the Staircase...")
        sleep(2)
        print("You Have Found the Treasure Room!")
        sleep(2)
        print("YOU WIN! :-D")
        #loop flag is now false and ends game
        return False
    else:
        print("You chose to Go Back...")
        sleep(2)
        #loop again through second scene
        return True

def cyoa():
    #print welcome
    print("Welcome to Adventure in the Forest!")
    print("Loading...")
    sleep(2)
    #create game status var
    first_status = first_scene()
    #check if player is still alive
    if first_status == False:
        sleep(2)
        print("YOU HAVE DIED :-X")
    else:
        #set a loop flag to check for go back status
        loop_flag = True
        while loop_flag:
            door_color = second_scene()
            if door_color == "BLUE":
                loop_flag = third_scene()
            else:
                loop_flag = fourth_scene()


#run game
cyoa()
