from django.urls import path
from .views import *
urlpatterns = [
    path('car-ads', CaradsView.as_view(), name='car-ads'),
    path('car-ads/add_img', CarImageViewSet.as_view(), name='add-img'),
    path('house-ads/add_img', HouseImageViewSet.as_view(), name='add_img'),
    path('catalog', CategoryView.as_view(), name='catalog'),
    path('house-ads', HouseadsView.as_view(), name='house-ads'),
    path('bot-users', BotUsersApiView.as_view(), name='bot-users'),
    path('feedbacks', FeedbacksApiView.as_view(), name='feedbacks'),
]
