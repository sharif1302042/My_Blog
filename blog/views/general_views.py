from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post


class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'new_index.html'

    def get(self, request):
        post = Post.objects.all().order_by('-updated_at')
        print(post)
        return Response({'post': post}, status=status.HTTP_200_OK)