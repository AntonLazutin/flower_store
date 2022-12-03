from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Flower(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

    def reduce_quantity(self, val):
        self.quantity = self.quantity - val
        self.save()




class Order(models.Model):
    is_cleaned = False
    customer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Заказ пользователя {self.customer.username}."
    
    def get_total_price(self):
        return self.quantity*self.flower.price

    # def clean(self):
    #     if self.quantity > self.flower.quantity:
    #         raise ValidationError("Количество не может превышать количество цветов!")
    #     else:
    #         self.is_cleaned=True

    # def save(self, *args, **kwargs):
    #     if not self.is_cleaned:
    #         self.full_clean()
    #     super(Order, self).save(*args, **kwargs)

    def execute_order(self):
        self.flower.reduce_quantity(self.quantity)
        self.flower.save()
        self.delete()
