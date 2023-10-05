from .models import Post, Category
from .serializers import PostSerializer, PostSerializerMultiLanguage
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
    queryset = Post.objects.language('en-us').only('translations', 'image', 'category')
    serializer_class = PostSerializerMultiLanguage


class PostListApiAR(ListAPIView):
    queryset = Post.objects.language('ar-sa').only('translations', 'image', 'category')
    serializer_class = PostSerializerMultiLanguage


"""@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request, slug):
    post = get_object_or_404(Post, slug=slug)
    data = PostSerializer(post).data
    return Response({'data':data})"""

class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.language('en-us').only('translations', 'image', 'category')
    serializer_class = PostSerializerMultiLanguage

class PostDetailApiAR(RetrieveAPIView):
    queryset = Post.objects.language('ar-sa').only('translations', 'image', 'category')
    serializer_class = PostSerializerMultiLanguage

"""def get_serializer_context(self):
    context = super().get_serializer_context()
    context['categories'] = Category.objects.only('name').annotate(post_count=Count('post_category'))
    context['tags'] = Tag.objects.all()
    context['related_posts'] = Post.objects.filter(category=self.get_object().category)[:3]
    return {'context':context}"""


"""@api_view(['GET'])
def post_search_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) &
        Q(description__icontains=query)
    )
    data = PostSerializerMultiLanguage(posts, many=True, context={"request":request}).data
    return Response({'data':data})"""


class PostsByFilters(ListAPIView):
    queryset = Post.objects.language('en-us').only('translations', 'image', 'category')
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        object_list = Post.objects.language('en-us').filter(
            Q(category__translations__title__icontains=slug)
        )
        posts = Post.objects.language('en-us').filter(
            Q(translations__title__icontains=slug) |
            Q(translations__description__icontains=slug)
        )
        slug = self.kwargs['slug']
        tags = Post.objects.language('en-us').filter(
            Q(tags__name__icontains=slug)
        )
        data = PostSerializerMultiLanguage(object_list, many=True, context={"request":request}).data
        data2 = PostSerializerMultiLanguage(posts, many=True, context={"request": request}).data
        data3 = PostSerializerMultiLanguage(tags, many=True, context={'request': request}).data
        return Response({'category':data, 'posts':data2, 'tags':data3})




class PostsByFiltersAR(ListAPIView):
    queryset = Post.objects.language('ar-sa').only('translations', 'image', 'category')
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        object_list = Post.objects.language('ar-sa').filter(
            Q(category__translations__title__icontains=slug)
        )
        posts = Post.objects.language('ar-sa').filter(
            Q(translations__title__icontains=slug) |
            Q(translations__description__icontains=slug)
        )
        slug = self.kwargs['slug']
        tags = Post.objects.language('ar-sa').filter(
            Q(tags__name__icontains=slug)
        )
        data = PostSerializerMultiLanguage(object_list, many=True, context={"request":request}).data
        data2 = PostSerializerMultiLanguage(posts, many=True, context={"request": request}).data
        data3 = PostSerializerMultiLanguage(tags, many=True, context={'request': request}).data
        return Response({'post by category':data, 'post by its name':data2, 'post by tag':data3})


"""@api_view(['GET'])
def blog_filters(request, slug):
    object_list = Post.objects.filter(
        Q(category__translations__title__icontains=slug)
    )
    posts = Post.objects.filter(
        Q(translations__title__icontains=slug) |
        Q(translations__description__icontains=slug)
    )
    data = PostSerializerMultiLanguage(object_list, many=True, context={"request": request}).data
    data2 = PostSerializerMultiLanguage(posts, many=True, context={"request": request}).data
    return Response({'category': data, 'posts': data2})"""

"""def list(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request':request,'slug':self.kwargs.get(self.lookup_url_kwarg)})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)"""


"""class PostsByTags(ListAPIView):
    queryset = Post.objects.only('slug', 'title', 'tags', 'image')
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        tags = Post.objects.filter(
            Q(tags__title__icontains=slug)
        )
        data = PostSerializer(tags, many=True, context={'request':request}).data
        return Response({'data': data})"""




























