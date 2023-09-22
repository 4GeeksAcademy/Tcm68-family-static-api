"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
initial_family_data = [{
    "name": "John",
    "age": "33",
    "lucky number": [ 7, 13, 22]
}, {
    "name": "Jane",
    "age": "35",
    "lucky number": [ 10, 14, 3]
}, {
    "name": "Jimmy",
    "age": "5",
    "lucky number": [ 1 ]
}]
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "name": "John",
            "age": "33",
            "lucky number": [ 7, 13, 22]
        }, {
            "id": self._generateId(),
            "name": "Jane",
            "age": "35",
            "lucky number": [ 10, 14, 3]
        }, {
            "id": self._generateId(),
            "name": "Jimmy",
            "age": "5",
            "lucky number": [ 1 ]
        }]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        return True
    
    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"]== int(id):
                self._members.pop(position)
                return True
            
    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member
            
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members