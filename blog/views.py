from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Blog
from blog.serializers import BlogSerializer
from rest_framework import permissions
from django.http import Http404


class BlogList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, blog_id):
        try:
            return Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, req, blog_id, format=None):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, blog_id, format=None):
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, blog_id, format=None):
        blog = self.get_object(blog_id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
