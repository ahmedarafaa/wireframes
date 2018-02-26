class Memmber(object):
    """docstring forMemmber."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.memberId   = memberId
        # print 'Memmber'

    def __repr__(self):

        return 'Name:{} , Age:{}'.format(self.name, self.age)


class Post(object):
    """docstring forPost."""

    def __init__(self, address, content):
        self.address = address
        self.content = content
        # print 'Post'

    def __repr__(self):
        return 'Address:{} , Content:{}'.format(self.address, self.content)
