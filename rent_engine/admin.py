from django.contrib import admin

from rent_engine.models import CategoryInformation, BooksCatalogue, BooksRented, Customer

admin.site.register(CategoryInformation)
admin.site.register(BooksCatalogue)
admin.site.register(BooksRented)
admin.site.register(Customer)