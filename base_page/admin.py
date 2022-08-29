from django.contrib import admin

from base_page.models import News, Bio, MyPhoto, PhotoAlbum, Video


@admin.register(PhotoAlbum)
@admin.register(MyPhoto)
class AdminPhoto(admin.ModelAdmin):
    list_display = ('id', 'name', 'admin_photo', 'date', 'is_published')
    list_display_links = ('name',)
    search_fields = ('name', 'date')
    list_filter = ('date', 'is_published', 'name')
    readonly_field = ('date', 'admin_photo')
    list_editable = ('is_published',)
    list_per_page = 10


@admin.register(Bio)
class AdminBio(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'admin_photo', 'date')
    list_display_links = ('title',)
    list_per_page = 10

    def has_add_permission(self, request):
        base_add_permission = super(AdminBio, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            count = Bio.objects.all().count()
            if count == 0:
                return True
        return False


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'date')
    list_filter = ('date', 'is_published', 'title')
    list_editable = ('is_published',)
    list_per_page = 5


@admin.register(Video)
class AdminVideo(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'date', 'is_published')
    list_display_links = ('name',)
    search_fields = ('name', 'date')
    list_filter = ('date', 'name', 'is_published')
    list_editable = ('is_published',)
    list_per_page = 10

