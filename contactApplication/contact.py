#json is a format in python used to temporarily store data
import json

class Contact:
    def __init__(self,file_path):
        self.json_file=file_path

    def get_contact(self):
        with open(self.json_file,"r") as user_data:
            self.user_data=json.load(user_data)
            return self.user_data





#this method helps to save contact in the database
    def update_contact(self,contact_dict: dict):
        with open(self.json_file,"w") as user_data:
            json.dump(contact_dict,user_data,indent=4)
        with open(self.json_file,"r")as user_data:
            new_data=json.load(user_data)
            return new_data
     
