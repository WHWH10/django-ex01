from django.urls import include, path
from commentapp.views import CommentCreateView, CommentDeleteView

app_name = "commentapp"
urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="create"),
    path("delete/", CommentDeleteView.as_view(), name="delete"),
]
