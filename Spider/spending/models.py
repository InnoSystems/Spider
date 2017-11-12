from django.db import models

class Shopping(models.Model):
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    store_name = models.CharField(max_length=255)
    shop_date = models.DateTimeField('date published')
    
    def __str__(self):
        return 'sum = "%s" store_name = "%s" shop_date= "%s"' % (self.sum.__str__(), self.store_name.__str__(), self.shop_date.__str__())
    
class Article(models.Model):
    Shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return 'name = "%s" price = "%s"' % (self.name.__str__(), self.price.__str__()) 