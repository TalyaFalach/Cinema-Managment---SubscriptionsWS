import requests
from DAL.members_dal import MembersDAL


class MembersBL:
    def __init__(self):
        self.__members = MembersDAL()

    def get_all_members(self):
        members = self.__members.get_all_members()
        return members

    def get_member(self, id):
        member = self.__members.get_member(id)
        return member

    def add_member(self, obj):
        member = self.__members.add_member(obj)
        return member

    def update_member(self, id, obj):
        member = self.__members.update_member(id, obj)
        return member

    def delete_member(self, id):
        member = self.__members.delete_member(id)
        return member

    # def add_user(self, obj):
    #     status = self.__users.add_user(obj)
    #     return status

    # def update_user(self, id, obj):
    #     status = self.__users.update_user(id, obj)
    #     return status

    # def delete_user(self, id):
    #     status = self.__users.delete_user(id)
    #     return status
