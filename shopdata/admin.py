from django.contrib import admin
from shopdata.models import Contact, Orders, Post, blogcomment


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_filter = ['name']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders)
admin.site.register(Post)
admin.site.register(blogcomment)

