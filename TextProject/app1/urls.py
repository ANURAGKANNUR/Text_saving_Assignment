
from django.urls import path
from .views import SnippetDetail,TagList,SnippetCreate,SnippetUpdate,TagListLinkedSnippets,SnippetList,TagCreate
urlpatterns = [
    path('list/', SnippetList.as_view(), name="list"),
    path('<int:pk>/',SnippetDetail.as_view(),name="snippet-detail"),
    path('create/',SnippetCreate.as_view(),name='create'),
    path('update/<int:pk>/',SnippetUpdate.as_view(),name='update'),
    path('tag/', TagList.as_view(), name='tag-list'),
    path('tag/<int:pk>/',TagListLinkedSnippets.as_view(),name='snippet'),
    path('tag/create/',TagCreate.as_view(),name='tag create')
    # path('delete/<int:pk>/',SnippetDelete.as_view(),name="delete")
    # path('<int:pk>/',Snippet1.as_view(),name="delete")


]
