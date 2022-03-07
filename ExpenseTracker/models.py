from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from djmoney.models.fields import MoneyField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    prof_pic = models.ImageField(upload_to='pictures/', default='default.png')
    name = models.CharField(max_length=50)
    bio = models.TextField()
    Savings = models.IntegerField(null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term).all()

    def __str__(self):
        return f'{self.user.username} Profile'


ADD_EXPENSE_CHOICES = [
    ("Expense", "Expense"),
    ("Income", "Income")
]


class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    add_money = models.CharField(max_length=10, choices=ADD_EXPENSE_CHOICES)
    quantity = MoneyField(max_digits=14, decimal_places=2,default_currency='KSH ')
    Date = models.DateField(auto_now_add=True)

    Category = models.ForeignKey(
        category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_expense(self):
        self.save()

    def delete_expense(self):
        self.delete()

    @classmethod
    def search_expense(cls, search_term):
        expenses = cls.objects.filter(
            Category__name__icontains=search_term).all()
        return expenses

    @classmethod
    def all_expensess(cls):
        return cls.objects.all()

    @classmethod
    def get_expense_by_id(cls, id):
        expense = Expense.objects.filter(id=id)
        return expense

    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ["-pk"]
