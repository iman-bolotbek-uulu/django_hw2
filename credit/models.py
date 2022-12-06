from django.db import models
import string
import random


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False,verbose_name='ФИО клиента')
    citizenship = models.CharField(max_length=20, null=False, blank=False, default='Кыргызстан',verbose_name='гражданство')
    birth_year = models.DateField(null=False, blank=False, auto_now_add=True,verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, null=True, blank=True,verbose_name='Место работы')
    update_date = models.DateField(auto_now=True,verbose_name='Дата последнего обновления')

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, null=False,blank=False,verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, null=False,verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    class Mete:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField(null=False, blank=False, verbose_name='Сумма кредита')
    date = models.DateField(auto_now_add=True, verbose_name='Дата получения кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')

    class Mete:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return self.sum


def id_generator(size=16, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))









