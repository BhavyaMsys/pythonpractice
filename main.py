# class Institute:
#     name_of_institute = "MsysTechnologies India PVT. Ltd." # class Varibale
#     def __init__(self,dirctor_name,work):
#         self.director_name = dirctor_name # instance varible
#         self.work = work # instance varible
#     def show_detail(self): # instance method
#         print("Name Of Institute",self.name_of_institute)
#         print("Name Of Director",self.director_name)
#         print("Work Of Institute",self.work)

# type of modes
# read mode "r"
# reading and writing mode "r+"
# reading in binary mode "rb"
# reading and writing in binary mode "rb+"
# writing mode "w"
# writing and reading mode "w+"
# writing in binary mode "wb"
# writing and reading mode in binary "wb+"
# append mode "a"
# append and reading "a+"
# exclusive mode x

import json
import random

class Institute:
    "This is application for training new joiner"
    name_of_institute = "MsysTechnologies India PVT. Ltd." # class Varibale
    def add_trainner(self,name_of_trainer,name_of_technology):
        self.name_of_trainer = name_of_trainer
        self.name_of_technology = name_of_technology
        id = random.randint(1000,2000)
        data_dict = {
            "trainers":[
                {   "trainerId":id,
                    "name":self.name_of_trainer,
                    "technology":self.name_of_technology
                }
            ]
        }
        with open("application\data.json","w",encoding="utf-8") as file:
            data = json.dump(data_dict)
            file.write(data)
            return data_dict["trainers"]
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

    
                



    
                    







