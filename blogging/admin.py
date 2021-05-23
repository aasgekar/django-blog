from django.contrib import admin
from blogging.models import Category, Post


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]

    class meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
# enter post and associate post with one or more categories
# remove ability from category to add posts to a category
