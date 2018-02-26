import models
import stores

member1 = models.Memmber('Ahmed', '20')
member2 = models.Memmber('Arafa', '30')


post1 = models.Post('x', 'x')
post2 = models.Post('y', 'y')
post3 = models.Post('z', 'z')


member_store = stores.MemberStore()
member_store.add(member1)
member_store.add(member2)
# print member_store.add(member1)
print member_store.get_all()


getAllMembers = stores.MemberStore()
# print getAllMembers.get_all()
# '{}'.format(getAllMembers)
