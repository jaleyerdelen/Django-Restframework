from rest_framework import serializers
from news.models import Article, Journalist

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince


class ArticleSerializer(serializers.ModelSerializer):
    #serializer field'ındaki key kısmı bu class sayesinde manipüle edebiliyoruz.
    time_since_pub = serializers.SerializerMethodField()
    #author = JournalistSerializer()
    #author = serializers.StringRelatedField() #modelsin içindeki str methodunu alır field'ın içine ekler
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
    #SerializerMethodField(method_name=None) bu şekilde yazmadığımız için doc. da başına get koyarak kullanın diyor.
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

class JournalistSerializer(serializers.ModelSerializer):
    #bu kodun amacı yeni yazar yaratabilmemiz diğer türlü hep hata veriyor yeni yazar yaratmıyordu.
    # read_only dememizin nedeni de makale vermeden yeni yazar yaratabilmek
    #articles = ArticleSerializer(many=True, read_only=True) #buradaki articles modelsin içindeki related_name

#author url sayfasında article'lar url şeklinde geliyor ve yeni yazar yaratabiliyoruz
    articles = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = "article-detail",
    )

    class Meta:
        model = Journalist
        fields = "__all__"