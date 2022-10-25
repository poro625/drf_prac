from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer


@api_view(['GET'])    # @api_view는 rest_framework에서 간단하게 사용할 수 있게 하여(브라우저블 api라고 한다) 브라우저에서 직접 조작 할 수 있게 한다
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data) #Response안에 담을 수 있는것은 딕셔너리 또는 스트링 밖에 없다.
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else :
        return Response(serializer.errors)

# Article 모델에서 -----> Json 모델로 바꾸는 방식 =  serializing
# Json 모델 -------> Article 모델로 바꾸는 방식 = deserializing 