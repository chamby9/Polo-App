# Imports

import pymongo
import json
from player import Player
from team import Team
from serializers import object_to_json

# Database
client = pymongo.MongoClient("mongodb+srv://admin-matt:Test123@cluster0.dhn88.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = client["poloApp"]
playerCol = mydb["players"]
teamCol = mydb["teams"]

# Test data
# mattChambers = Player(1, "Matthew", "Chambers", 9, 1)
# sacs19A = Team(1, "Ryan Weideman", "Dave Mckinnon", "SACS", "u19")
# playerJSON = object_to_dict(mattChambers)
# teamJSON = object_to_dict(sacs19A)
# print(type(playerJSON))
# print(type(teamJSON))

def menu():
    active = True

    while(active == True):
        print("MAIN MENU\n")
        print("1. Create Player\n2. Create Team\n3. View Player Details\n4. View Team Details\n5. Exit")

        choice = int(input("What is your selection?(numbers only): "))
        if(choice == 1):
            newPlayer = Player
            Player.createPlayer(newPlayer)
            jsonPlayer = object_to_json(newPlayer)

            print(type(jsonPlayer))
            # playerCol.insert_one(newPlayer)
            active = False

        elif(choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass
        elif(choice == 5):
            print("Goodbye")
            active = False
        else:
            print("Please choose a valid option\n\n\n")

menu()
