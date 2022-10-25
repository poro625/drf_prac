from dataclasses import fields

# 우리가 view에서 하나하나 변수를 선언하여 어떠한것을 담아주는것이 귀찮고 반복적이고 불필요한 작업이라고 생각될 수 있다
# 이러한 작업들을 자동화 시키기 위해서 장고 rest_framework에서 serializers기능을 사용하는 것이다. 
# 이것을 직렬화라 말할것이며, 오브젝트 구조를 스트링 으로 바꾸는것이라고 한다

from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"