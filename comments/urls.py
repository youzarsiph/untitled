""" URLConf for untitled.comments """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from untitled.comments.views import CommentViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("comments", CommentViewSet, "comment")

urlpatterns = [
    path("", include(router.urls)),
]
