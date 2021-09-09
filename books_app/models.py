from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Books(models.Model):

    status_book=[
        ('availble','availble'),
        ('rent','rent'),
        ('sold','sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='books', blank=True, null=True)
    author_photo = models.ImageField(upload_to='author', blank=True, null=True)
    prices = models.DecimalField(max_digits=5,decimal_places=2)
    retail_price_day = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retail_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book)
    pages = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)