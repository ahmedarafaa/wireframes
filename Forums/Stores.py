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
        # append member

    def get_by_id(self, memberid):
        all_members = self.get_all()
        for member in all_members:
            if member.id == memberid:
                return member

    def entity_exists(self, member):
        # check if member exist or not
        get_id = self.get_by_id()
        if member in get_id:
            return True

    def delete(self, memberid):
        # Remove if exist
        if memberid in self.get_by_id:
            self.members.remove(memberid)

