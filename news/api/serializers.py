from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    published = serializers.DateField()
    active = serializers.BooleanField()
    create_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    #kwargs kullanılmasının nedeni validate_data'nın arka tarafta dictionary gelmesidir.
    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #dönen validate data'ya bak author'ı kontrol et eğer author'ın karşısında değer varsa bunu al yoksa instance.author' kullan.
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.text = validated_data.get('text', instance.text)
        instance.city = validated_data.get('city', instance.city)
        instance.published = validated_data.get('published', instance.published)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance
        