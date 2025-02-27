from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializers import BlogSerializer, BlogOutputSerializer, ComentarioSerializer, ComentarioOutputSerializer
from .models import Blog, Comentario


# Create your views here.
class CreateBlogView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = BlogSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            blog = serializer.save()
            serializer = BlogOutputSerializer(blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class ListBlogView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            blogs = Blog.objects.all()
            serializer = BlogOutputSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class EditBlogView(APIView):
    permission_classes = [AllowAny]
    def patch(self, request, pk=None):
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(blog, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                serializer = BlogOutputSerializer(blog)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class DeleteBlogView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk=None):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.delete()
            return Response({"Eliminado satisfactoriamente"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:            
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ComenatarioView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            comentarios = ComentarioSerializer(data=request.data)
            comentarios.is_valid(raise_exception=True)
            coment_save = comentarios.save()
            comentarios = ComentarioOutputSerializer(coment_save)
            return Response(comentarios.data,status=status.HTTP_201_CREATED)
        except Exception as e:            
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

class ListComentarioView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            comentario = Comentario.objects.all()
            serializer = ComentarioOutputSerializer(comentario, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)