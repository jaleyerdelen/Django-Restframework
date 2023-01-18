from rest_framework import serializers
from news.models import Article

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince
class ArticleSerializer(serializers.ModelSerializer):
    
    #serializer field'ındaki key kısmı bu class sayesinde manipüle edebiliyoruz.
    time_since_pub = serializers.SerializerMethodField()
    class Meta:
        model = Article

        #bütün alanları getirir
        fields = "__all__"

        #sadece bu alanları getirir
        #fields = ["author", "title", "text"]

        #exlude ise o alanlar harici getirir
        #exclude = ["author", "title", "text"]

        read_only_fields = ["id", " create_date", "update_date"]

    #Serializer field kısmına value ekleyebiliyoruz
    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.published
        if object.active == True:
            time_delta = timesince(pub_date, now) #yayınlanma tarihinden bugüne kadar geçen süreyi hesaplıyor timesince sayesinde
            return time_delta
        else:
            return "it is not active"

    def validate_published(self, time_value):
        today = date.today()
        if time_value > today:
            raise serializers.ValidationError("published date can't be greater than today")
        return time_value

### STANDART SERIALIZER ###
class ArticleDefaultSerializer(serializers.Serializer):
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
    
    #custom validation
    def validate(self, data): #object level
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must not be the same")
        return data

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(f"Title must be at least 10 characters. You entered {len(value)} characters")
        return value
        