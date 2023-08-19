from .models import Post, Category
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from django.db.models import Q, Count
from taggit.models import Tag


"""@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_posts = Post.objects.only('slug','auther','title','tags','image')
    data = PostSerializer(all_posts, many=True, context={'request':request}).data
    return Response({'data':data})"""

class PostListApi(ListAPIView):
    queryset = Post.objects.only('slug', 'title', 'tags', 'image')
    serializer_class = PostSerializer

"""@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request, slug):
    post = get_object_or_404(Post, slug=slug)
    data = PostSerializer(post).data
    return Response({'data':data})"""

class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.only('slug', 'title', 'tags', 'image', 'created_at', 'description', 'category')
    serializer_class = PostSerializer

"""def get_serializer_context(self):
    context = super().get_serializer_context()
    context['categories'] = Category.objects.only('name').annotate(post_count=Count('post_category'))
    context['tags'] = Tag.objects.all()
    context['related_posts'] = Post.objects.filter(category=self.get_object().category)[:3]
    return {'context':context}"""


@api_view(['GET'])
def post_search_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) &
        Q(description__icontains=query)
    )
    data = PostSerializer(posts, many=True, context={"request":request}).data
    return Response({'data':data})


class PostsByCategory(ListAPIView):
    queryset = Post.objects.only('slug', 'title', 'tags', 'image')
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains=slug)
        )
        data = PostSerializer(object_list, many=True, context={"request":request}).data
        return Response({'data':data})




"""def list(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request':request,'slug':self.kwargs.get(self.lookup_url_kwarg)})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)"""


class PostsByTags(ListAPIView):
    queryset = Post.objects.only('slug', 'title', 'tags', 'image')
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(tags__name__icontains=slug)
        )
        data = PostSerializer(object_list, many=True, context={'request':request}).data
        return Response({'data': data})




























