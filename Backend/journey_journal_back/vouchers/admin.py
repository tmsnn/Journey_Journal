from django.contrib import admin

from .models import Voucher, Category, Comment, User

admin.site.register(Voucher)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)
