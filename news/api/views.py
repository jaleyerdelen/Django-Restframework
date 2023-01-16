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

@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(request, pk):
    try:
        article_instance = Article.objects.get(pk=pk)
    #Article içerisindeki id'ler yok ise
    except Article.DoesNotExist:
        return Response(
            {
                "errors": {
                    "code":404,
                    "message": f'({pk} is not found)'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
    #try blogundaki Article içerisindeki id'leri bulduysa bu blok çalışır
    if request.method == "GET":
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)

    elif request.method == "PUT":
        #article_instance veri tabanından çektiğim mevcut data
        #request.data ise güncellenecek verileri içeren istekten gelen yeni veri
        serializer = ArticleSerializer(article_instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article_instance.delete()
        return Response(
            {
                "success": {
                    "code":204,
                    "message": f'({pk} is deleted )'
                }
            },
            status = status.HTTP_204_NO_CONTENT
        )