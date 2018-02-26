class MemberStore():
    """docstring for MemberStore."""
    members = []

    def get_all(self):
        return MemberStore.members
        # get all members

    def add(self, member):
        return MemberStore.members.append(member)
        # append member
