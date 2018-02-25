import models
import Stores

member1 = models.Memmber('x', 'x')
member2 = models.Memmber('y', 'y')


post1 = models.Post('x', 'x')
post2 = models.Post('y', 'y')
post3 = models.Post('z', 'z')


member_store = Stores.MemberStore()
member_store.add(member1)
member_store.add(member2)
