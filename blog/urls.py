from django.urls import path
from blog.views import general_views,python_views

urlpatterns = [
    path('', general_views.Index.as_view(),name= 'blog'),

    #python
    path('python/string_operation/',python_views.StringOperation.as_view(),name = 'python/string_operation/'),
    path('python/list_operation/',python_views.ListOperation.as_view(),name = 'python/list_operation/'),
    path('python/built_in_function/',python_views.BuiltInFunction.as_view(),name = 'python/built_in_function/'),
]
