from django.contrib import admin
from .models import Shirt, Comment_of_shirt, Topic_of_shirts, Tag_for_shirts


admin.site.register(Comment_of_shirt)
admin.site.register(Topic_of_shirts)
admin.site.register(Tag_for_shirts)
# Register your models here.

class ShirtAdmin(admin.ModelAdmin):
    list_display = ('name_of_shirt', 'user', 'created_time', 'topic')
    list_filter = ('topic', 'created_time', 'user')
    #search_fields = ('title', 'body')
    #date_hierarchy = 'created_time'

admin.site.register(Shirt, ShirtAdmin)