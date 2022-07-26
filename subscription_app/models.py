# from django.contrib.auth.models import User
# from django.db import models
#
#
# # Create your models here.
# class Subscription(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     subscription = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription")
#
#     def __str__(self):
#         return self.user.username

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

MEMBERSHIP_CHOICES = (
    ('Premium', 'pre'),
    ('Free', 'free')
)

User = get_user_model()


class Membership(models.Model):
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default='Free',
        max_length=30
    )
    price = models.DecimalField(default=0, decimal_places=1, max_digits=100)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
