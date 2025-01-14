from django.contrib import admin
from blog.models import Tag,Category,Post
from django.utils.html import format_html
from django.urls import reverse


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    fields = ('name', 'status', 'is_nav')

    # 新增字段
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_time', 'owner', 'operator')
    list_display_links = []
    list_filter = ['category', ]
    search_fields = ['title', 'category']

    actions_on_top = True
    actions_on_bottom = False

    # 编辑页面
    save_on_top = True

    fields = (
        ('title', 'category'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        """新增编辑按钮"""
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=[obj.id]),
        )

    operator.short_description = "新年"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
