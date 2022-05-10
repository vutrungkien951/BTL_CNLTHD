from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')


class Port(ModelBase):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return "{}: {}".format(self.name, self.address)


class Ride(ModelBase):
    date_start = models.DateField()
    date_return = models.DateField()
    far = models.IntegerField()
    long = models.IntegerField()
    capacity = models.IntegerField()
    driver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='rides')
    ports = models.ManyToManyField(Port, related_name='rides')
    customer_list = models.ManyToManyField(User, related_name='booked_rides')

    def __str__(self):
        ports = self.ports.all()
        return '{} to {}'.format(ports[0], ports[len(ports)-1])


class FeedBack(ModelBase):
    rating = models.IntegerField()
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_feedback')
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='all_feedback')

    def __str__(self):
        return '{} feedback about {}'.format(self.user, self.ride)
