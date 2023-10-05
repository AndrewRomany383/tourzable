from django.contrib import admin
from django.contrib.admin import ModelAdmin
from parler.admin import TranslatableAdmin
from .models import Post, Category
# Register your models here.
class PostAdmin(TranslatableAdmin):
    list_display = ('title','tag_list', 'created_at', 'description', 'category', 'slug')
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    """def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.tags.add(extracted)"""

    fieldsets = (
        (None, {
            'fields': ('title', 'tags', 'image', 'created_at', 'description', 'category', 'slug'),
        }),
    )



class CategoryAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)









