from django.contrib.auth.models import User
from django.db import models

class BaseFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseFields):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.user.username


class CategoryInformation(BaseFields):
    CHOICES = (
        ('Regular', 'Regular'),
        ('Fiction', 'Fiction'),
        ('Novels', 'Novels'),
    )
    name = models.CharField(max_length=200, choices=CHOICES)
    version = models.IntegerField()
    rules = models.JSONField()

    class Meta:
        unique_together = ('name', 'version')

class BooksCatalogue(BaseFields):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryInformation, on_delete=models.CASCADE)

    def __str__(self):
        return '%s-%s' % (self.name, self.author)


class BooksRented(BaseFields):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(BooksCatalogue, on_delete=models.SET_NULL, null=True)
    date_rented = models.DateField()
    date_deposited = models.DateField()
    active = models.BooleanField(default=True)
    # due_date = models.DateField()

    class Meta:
        unique_together = ('customer', 'book', 'date_rented')

    @property
    def days_rented(self):
        if self.date_deposited is not None:
            return (self.date_deposited - self.date_rented).days

    def __str__(self):
        return '%s-%s' % (self.customer.user.username, self.book.name)