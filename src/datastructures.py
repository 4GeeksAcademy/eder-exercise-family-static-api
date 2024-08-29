
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self,last_name):
        self._next_id = 1      
        self.last_name = last_name   
        

        # example list of members
        self._members = [ {
    "id": 1,
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7,13,1]
},{
    "id": 2,
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10,14,3]
},{
    "id": 3,
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id =self._next_id
        self._next_id += 1
        return generated_id



    def add_member(self, member):        
        self._members.append(member)
        pass

    def delete_member(self, id):
        delete_specific_member = next((sub for sub in self._members if sub['id'] == id), None)
        self._members.remove(delete_specific_member)
        # fill this method and update the return
        pass

    def get_member(self, id):
        specific_member = next((sub for sub in self._members if sub['id'] == id), None)
        return specific_member
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
