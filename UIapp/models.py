from pickle import TRUE
from django.db import models



class Bank_Customer(models.Model):
    BBranch=(
        ('Poonamalle','Poonamalle'),
        ('Sholinganallur','Sholinganallur'),
        ('Avadi','Avadi'),
        ('Nellore','Nellore'),
        ('kadapa','kadapa')

    )

    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Account_Number=models.BigIntegerField()
    IFSC_code=models.CharField(max_length=50)
    Branch=models.CharField(max_length=100,choices=BBranch)
    Mobile_NO=models.BigIntegerField()
    Email_id=models.EmailField()
    Address=models.TextField()
    def choice(self):
        return dict(Bank_Customer.BBranch)




