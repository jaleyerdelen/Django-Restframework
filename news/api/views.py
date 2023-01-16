from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article
from news.api.serializers import ArticleSerializer

@api_view(["GET", "POST"])
def article_list_create_api_view(request):
    
    if request.method == "GET":
        article = Article.objects.filter(active=True)
        #article sonucunda bize bir query veriyor obje değil o yüzden many=True diye belirttim yoksa hata veriyor. 
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)