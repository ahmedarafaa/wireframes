class MemberStore():
    """docstring for MemberStore."""
    members = []
    last_id = 0

    def get_all(self):
        return MemberStore.members
        # get all members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, memberid):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if memberid == member.id:
                result = member
                break
        return result

    def entity_exists(self, memberid):
        get_id = self.get_by_id()
        if memberid in get_id:
            return True
        else:
            return False

    def delete(self, memberid):
        if memberid in self.get_by_id:
            self.members.remove(memberid)

