from json import JSONEncoder

import json

# Select a Team from the team data to assign team_id
    # Take in name and cap no.
    # Write to DB the team no.


class Player:
    def __init__(self, _id, first_name, last_name, cap_no, team_id):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.cap_no = cap_no
        self.team_id = team_id

    def getCap(self):
        
        return self.cap_no

    def createPlayer(self):
        set_player_activity = True

        while(set_player_activity == True):
            fname = input("First name:\n")
            lname = input("Last name:\n")
            capNo = int(input("Cap Number: "))
            team_id = 1
            
            answer = input(f"{fname}\n{lname}\n{capNo}\Are you happy with this? (Y/N)")

            if (answer.lower() == "y"):
                self._id = 6
                self.first_name = fname
                self.last_name = lname
                self.cap_no = capNo
                self.team_id = team_id
                set_player_activity = False
            else:
                pass

# newPlayer = Player

# newPlayer.createPlayer()

        
        






# jsonString = PlayerEncoder().encode(mattChambers)


