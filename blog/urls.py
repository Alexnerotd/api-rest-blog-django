from django.urls import path
from .views import POSTBlogView, GETBlogView, PUTBlogView, DELETEBlogView


urlpatterns = [
    path('create-blog/', POSTBlogView.as_view(), name='create-blog'),
    path('list-blogs/',GETBlogView.as_view(), name='list-blogs'),
    path('update-blog/<int:pk>/',PUTBlogView.as_view(), name='update-blogs'),
    path('delete-blog/<int:pk>/',DELETEBlogView.as_view(), name='delete-blogs'),
]
