from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post





class StringOperation(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'python/string_operation.html'

    def get(self, request):
        post = Post.objects.get(pk=3)
        previous = Post.objects.get(pk=2)
        if post:
            return Response({'post': post}, status=status.HTTP_200_OK)
        return Response({'post': post}, status=status.HTTP_200_OK)


class ListOperation(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'python/list_operation.html'

    def get(self, request):
        post = Post.objects.get(pk=2)
        previous = Post.objects.get(pk=1)
        next = Post.objects.get(pk=3)
        if post:
            return Response({'post': post,'previous':previous,'next':next}, status=status.HTTP_200_OK)
        return Response({'post': post}, status=status.HTTP_200_OK)


class BuiltInFunction(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'python/built_in_function.html'

    def get(self, request):
        post = Post.objects.get(pk=1)
        if post:
            return Response({'post': post}, status=status.HTTP_200_OK)
        return Response({'post': post}, status=status.HTTP_200_OK)
