from credit.models import Client,id_generator,Account,Credit
from django.utils import timezone
import string
import random

client = Client.objects.create(name='Berdiev N.D',birth_year=1994,work_place='Codify',update_date=timezone.now())
client1 = Client.objects.create(name='Bolotbek U.I',birth_year=2003,work_place='Google',update_date=timezone.now())

ac1 = client.accounts.create(number=id_generator(),account_type=1)
ac2 = client.accounts.create(number=id_generator(),account_type=1)
ac3 = client1.accounts.create(number=id_generator(),account_type=2)
ac4 = client1.accounts.create(number=id_generator(),account_type=2)

cr1 = ac1.credits.create(sum=100000,date=timezone.now)
cr2 = ac1.credits.create(sum=100000,date=timezone.now)
cr3 = ac1.credits.create(sum=100000,date=timezone.now)
cr4 = ac1.credits.create(sum=100000,date=timezone.now)













# ac1 = Account.objects.create(number=id_generator(),account_type=1,client=client)
# ac2 = Account.objects.create(number=id_generator(),account_type=2,client=client1)
#
# cr1 = Credit.objects.create(sum=100000,date=timezone.now(),account=client)
# cr2 = Credit.objects.create(sum=200000,date=timezone.now(),account=client1)



