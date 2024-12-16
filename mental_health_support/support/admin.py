from django.contrib import admin
from .models import Testimony, Photo, AISupport, Session, Post

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'date')
    search_fields = ('user__username', 'content')
    list_filter = ('date',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('url', 'description', 'date')
    search_fields = ('description',)
    list_filter = ('date',)

@admin.register(AISupport)
class AISupportAdmin(admin.ModelAdmin):
    list_display = ('user', 'issue_detected', 'date')
    search_fields = ('user__username', 'issue_detected')
    list_filter = ('date',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time', 'feedback')
    search_fields = ('user__username', 'feedback')
    list_filter = ('start_time', 'end_time')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updated_at')
    search_fields = ('user__username', 'text')
    list_filter = ('created_at', 'updated_at')
