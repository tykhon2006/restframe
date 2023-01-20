from .models import Post, Category
from rest_framework import generics, viewsets
from .serializers import PostSerializer, CatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAdminUser,)

# class PostAPIView(APIView):
#     def get(self, request):
#         lst = Post.objects.all()
#         return Response({"posts": PostSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Error": "Method PUT not allowed"})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"Error": "Object does not exist"})
#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         # код
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Error": "Method Delete not allowed"})
#         instance = Post.objects.get(pk=pk)
#         instance.delete()
#         return Response({"post": f"delete post {str(pk)}"})


# def put(self, request, *args, **kwargs):
#     pk = kwargs.get("pk", None)
#     if not pk:
#         return Response({"Error": "Method PUT not allowed"})
#     try:
#         instance = Post.objects.get(pk=pk)
#     except:
#         return Response({"Error": "Object does not exist"})
#     serializer = PostSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     instance.title = request.data["title"]
#     instance.content = request.data["content"]
#     instance.cat_id = request.data["cat_id"]
#     instance.save()
#     return Response({"post": PostSerializer(instance).data})

# Create your views here.
