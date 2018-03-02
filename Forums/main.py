import models
import stores

member1 = models.memmber('Ahmed', '20')
# member2 = models.memmber('Arafa', '30')

add_new_member = stores.MemberStore()
add_new_member.add(member1)
print add_new_member.get_all()
print add_new_member.last_id
add_new_member.delete(1)
print add_new_member.get_by_id(member1)
# post1 = models.Post('x', 'x')
# post2 = models.Post('y', 'y')
# post3 = models.Post('z', 'z')


