from django.contrib import admin

from .models import Author,Post

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('pk',)
    list_display = ('pk','username','full_name','total_post','created_at','updated_at',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('pk',)
    list_display = ('pk','author','title','category','url','updated_at',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)