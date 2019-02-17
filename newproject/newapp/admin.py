from django.contrib import admin
from newapp.models import Author
from newapp.models import Book

# admin.register(Author)
# admin.register(Book)

class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)