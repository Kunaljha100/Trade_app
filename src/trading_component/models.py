from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils import timezone





class User(AbstractUser):
    is_order_user = models.BooleanField(default=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



ORDER_CHOICES = (
    ("Buy", "Buy"),
    ("Sell", "Sell"),
    
)

class order(models.Model):
    entry_price=models.CharField(max_length=50)
    quantity = models.CharField(max_length=150)
    trade_type=models.CharField(max_length=20,choices = ORDER_CHOICES)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering = ['trade_type',]



    def __str__(self):
        return f"{self.user} {self.trade_type}"

    
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)


