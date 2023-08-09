from django.db import models

class Software(models.Model):
    title = models.CharField('Title', max_length=256, db_index=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    currency = models.CharField('Currency', max_length=30)
    count = models.PositiveSmallIntegerField('Count')    

    class Meta:
        verbose_name = 'Software'
        verbose_name_plural = 'Software'
        ordering = ('price',)

    def __str__(self) -> str:
        return str(self.title).strip()
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'currency': self.currency,
            'count': self.count
        }