from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class  Element(models.Model):
    symbol=models.CharField(max_length=5)
    atomic_number = models.IntegerField()#models.TextField(max_length=60,default='')
#    category= models.ForeignKey(Category , on_delete=models.CASCADE)
#    picture = models.ImageField(upload_to='upload/product/')
#    picture1 = models.ImageField(upload_to='upload/product/' , default="media/upload/product/Untitled_bVsdsDX.jpg")
#    kilo = models.BooleanField(default=True , blank= True)
#    price = models.IntegerField(max_length=20,default=1)
#    
#    is_importmant = models.BooleanField(default=False , blank= True)
#    size = models.ForeignKey(Pro,on_delete = models.CASCADE)
    atomic_mass = models.DecimalField(max_digits=18,decimal_places=12,validators=[MinValueValidator(Decimal('0'))])
    category = models.CharField(max_length=10)
    ntm = models.CharField(max_length=10)
    isotopes=models.CharField(max_length=10)
    ionic_compounds=models.CharField(max_length=10)
    Applications=models.CharField(max_length=10)
    History=models.CharField(max_length=10)
    discoverer=models.CharField(max_length=10)
    tod=models.CharField(max_length=10)
    Safety=models.CharField(max_length=30)
    interesting_facts=models.CharField(max_length=70)
    
    
    
    
    #1 Applications2 3 4 Time of discovery5 Safety6 
    #
    def __str__(self):
        return self.symbol