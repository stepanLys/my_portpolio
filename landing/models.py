from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return "Заказ %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Всі замовлення'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)