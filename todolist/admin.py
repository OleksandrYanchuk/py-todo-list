from django.contrib import admin

from todolist.models import Tag, Task


@admin.register(Task)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("content", "status")
    list_filter = ("tags",)


admin.site.register(Tag)
