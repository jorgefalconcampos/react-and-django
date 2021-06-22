from django.db import models as m

# Create your models here.


    


class Customer(m.Model):
    first_name = m.CharField("First name", max_length=255)
    last_name = m.CharField("Last name", max_length=255)
    email = m.EmailField()
    phone = m.CharField(max_length=20)
    address = m.TextField(blank=True, null=True)
    description = m.TextField(blank=True, null=True)
    createdAt = m.DateField("Created at",auto_now_add=True)

    def __str__(self):
        return self.first_name