from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status


@api_view(['GET', 'POST'])    # @api_view는 rest_framework에서 간단하게 사용할 수 있게 하여(브라우저블 api라고 한다) 브라우저에서 직접 조작 할 수 있게 한다
def articleAPI(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data) #Response안에 담을 수 있는것은 딕셔너리 또는 스트링 밖에 없다.
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Article 모델에서 -----> Json 모델로 바꾸는 방식 =  serializing
# Json 모델 -------> Article 모델로 바꾸는 방식 = deserializing 

@api_view(['GET', 'PUT', 'DELETE'])    # @api_view는 rest_framework에서 간단하게 사용할 수 있게 하여(브라우저블 api라고 한다) 브라우저에서 직접 조작 할 수 있게 한다
def articledetailAPI(request, article_id):
    if request.method == 'GET':        
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
