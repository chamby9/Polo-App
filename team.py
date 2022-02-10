from json import JSONEncoder

import json


class Team:
    def __init__(self, _id, coach, manager, school, age_group):
        self._id = _id
        self.coach = coach
        self.manager = manager
        self.school = school
        self.age_group = age_group
   
    def toString(self):
        print(f"Team: {self.name + self.age_group}")
        print(f"Players:\n{self.players}")
        print(f"Coach: {self.coach}")
        print(f"Manager/Assistant Coach: {self.manager}")

    def getSchool(self):
        return self.school




# jsonString = PlayerEncoder().encode(mattChambers)



