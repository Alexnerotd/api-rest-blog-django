from django.urls import path
from .views import POSTBlogView


urlpatterns = [
    path('create-blog/', POSTBlogView.as_view(), name='create-blog'),
]
