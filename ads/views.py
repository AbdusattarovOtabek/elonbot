from rest_framework.generics import CreateAPIView
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView

class BotUsersApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class  = BotUserSerializer

class FeedbacksApiView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class  = FeedbackSerializer

class CaradsView(ListCreateAPIView):
    queryset = Carads.objects.filter(status=True)
    serializer_class = CaradsSerializer

class CarImageViewSet(CreateAPIView):  
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer

class HouseadsView(ListCreateAPIView):
    queryset = Houseads.objects.filter(status=True)
    serializer_class = HouseadsSerializer

class HouseImageViewSet(CreateAPIView):
    queryset = HouseImage.objects.all()
    serializer_class = HouseImageSerializer

class CategoryView(ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
