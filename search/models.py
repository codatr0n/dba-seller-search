from django.db import models

# Create your models here.


class Seller(models.Model):
    dba_id = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Listing(models.Model):
    external_id = models.IntegerField(blank=False)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=200)
    dba_url = models.URLField(max_length=1000)
    img_url = models.URLField(max_length=1000)
    last_updated = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return '{snippet}...'.format(snippet=self.name[:60])
