
class detail:
    def __init__(self,firstname,lastname,introduction):
        self.firstname=firstname
        self.secondname=lastname
        self.introduction = introduction

        self.firstname=input("enter your firstname: ")
        self.secondname=input("enter your secondname: ")
        self.introduction =input("Tell something about you: ")
        self.save_to_history()

    def save_to_history(self):
        with open("history.txt", "a") as file:
         file.write(f"Name:{self.firstname} {self.secondname} Introduction: {self.introduction}\n")


    def intro(self):
        print(f"My name is {self.firstname,self.secondname, self.introduction}")
