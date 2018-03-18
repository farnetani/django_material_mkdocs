from django.conf.urls import url


from .views import serve_docs


urlpatterns = [
    url(r'^(?P<path>.*)$', serve_docs),
]
