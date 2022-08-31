from django.db.models import Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer,TagSerializer,SnippetSerializerUrl,TagSerializerURL
from .models import Snippet,Tag
from rest_framework import generics
# Create your views here.
class TagList(generics.ListAPIView):  # TO view the TAG list
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagListLinkedSnippets(generics.ListAPIView):  # to retrive the snippet linked to a tag
    permission_classes = [IsAuthenticated]
    serializer_class = SnippetSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        return  Snippet.objects.filter(tag=pk)

class SnippetCreate(generics.CreateAPIView):   #To add the Snippet
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     return Snippet.objects.all()

    def perform_create(self, serializer):
        createdby=self.request.user
        snippet_queryset=Snippet.objects.all()
        serializer.save(createdby=createdby)

class SnippetUpdate(generics.RetrieveUpdateAPIView):  #update snippet
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly]

class SnippetDetail(APIView):   #Snippet detail view for all users and owner can delete the snippet
    def get(self,request,pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            serializer=SnippetSerializer(snippet)
            return Response(serializer.data)
        except snippet.DoesNotExist:
            return Response({'error':'snippet Not found'},status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsOwnerOrReadOnly,])
    def delete(self,request,pk):
        snippet=Snippet.objects.get(pk=pk)
        serializer=SnippetSerializer(snippet)
        snippet.delete()
        return Response(serializer.data,status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated,])
class SnippetList(APIView):         #to view the url of snippets and count
    def get(self,request):
        snippets=Snippet.objects.all()
        count=Snippet.objects.count()
        # print(count)
        # count=Count(snippets)
        serializer=SnippetSerializerUrl(snippets,many=True,context={'request':request,'count':count})
        return Response(serializer.data)

@permission_classes([IsAuthenticated,])
class TagCreate(APIView):
    def post(self,request):
        serializer=TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



