import json
import random

class Institute:
    "This is application for training new joiner"
    name_of_institute = "MsysTechnologies India PVT. Ltd." # class Varibale
    def add_trainner(self,name_of_trainer,name_of_technology,active=False):
        self.name_of_trainer = name_of_trainer
        self.name_of_technology = name_of_technology
        id = random.randint(1000,2000)
        data_dict = {}
        try:
            with open("application\data.json","r",encoding="utf-8") as file:
                data = json.loads(file.read())
            data["trainers"].append(
                    {   "trainerId":id,
                    "name":self.name_of_trainer,
                    "technology":self.name_of_technology,
                    "active":eval(active.title())
                }
            )
            data_dict = data
        except:
            data_dict = {
                "trainers":[
                    {   "trainerId":id,
                        "name":self.name_of_trainer,
                        "technology":self.name_of_technology,
                        "active":eval(active.title())
                    }
                ]
            }
        with open("application\data.json","w",encoding="utf-8") as file:
            data = json.dumps(data_dict)
            file.write(data)
            return print(
                "TrainerId",id,"\n",
                "Name",self.name_of_trainer,"\n"
                "Technology",self.name_of_technology,"\n"
                "Active",eval(active.title()))

    def get_trainer_by_technology(self,technology_name):
        self.filter_technology_list = []
        with open("application\data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainers"]
            for trainer in trainer_list:
                if trainer["Technology"]==technology_name:
                    self.filter_technology_list.append(trainer)
        return self.filter_technology_list

    def get_trainer_by_name(self,trainer_name):
        self.filter_name_list = []
        with open("application\data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainers"]
            for trainer in trainer_list:
                if trainer["Name"]==trainer_name:
                    self.filter_name_list.append(trainer)
        return self.filter_name_list
    
    def get_trainer_by_id(self,trainer_id):
        self.filter_name_list = []
        with open("application\data.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            trainer_list = data["trainers"]
            for trainer in trainer_list:
                if trainer["trainerId"]==trainer_id:
                    self.filter_name_list.append(trainer)
        return self.filter_name_list

obj = Institute()  

while True:

    name = str(input("enter the name:"))
    tech = str(input("enter the technology name:"))
    active = str(input("enter the status:"))

    obj.add_trainner(name,tech,active)