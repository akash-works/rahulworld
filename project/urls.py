from django.urls import path,include
from .views import *
from  django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",index,name="index.html"),
    path("blog/",blog,name="blog.html"),
    path("about/",about,name="about.html"),
    path("contact/",contact,name="contact.html"),
    path("services/",services,name="services.html"),
    path("team/",team,name="team.html"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)