from django.urls import path


from .views import Context


urlpatterns = [

     path('', Context.as_view()),


]
