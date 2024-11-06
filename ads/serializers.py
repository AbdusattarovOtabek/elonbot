from ads.models import *
from rest_framework.serializers import ModelSerializer



class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'

class HouseImageSerializer(ModelSerializer):
    class Meta:
        model = HouseImage
        fields = ['house', 'img']

class CarImageSerializer(ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['car', 'img']

class HouseadsSerializer(ModelSerializer):
    img = HouseImageSerializer(many=True, read_only=True)  # Rasmlar qo'shilmoqda

    class Meta:
        model = Houseads
        fields = '__all__'

class CaradsSerializer(ModelSerializer):
    img = CarImageSerializer(many=True, read_only=True)  

    class Meta:
        model = Carads
        fields = '__all__'



class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
       
class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("user_id",  "created_at", "body")