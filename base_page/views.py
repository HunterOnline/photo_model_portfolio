from base_page.models import News, Bio, PhotoAlbum, MyPhoto, Video
from django.views.generic.list import ListView


class Context(ListView):
    model = News

    context_object_name = 'articles'
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bio_mod'] = Bio.objects.all()[0]
        context['photo_mod'] = PhotoAlbum.objects.filter(is_published=True)
        context['my_photo_mod'] = MyPhoto.objects.filter(is_published=True)
        context['video_link'] = Video.objects.filter(is_published=True)

        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)
