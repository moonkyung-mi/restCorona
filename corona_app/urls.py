from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='corona_app')
    path("hello/", helloAPI), # hello/ 요청이 들어오면 helloAPI 함수 호출
    path("copop/", CoPopuDensityAPI), # copop/ 요청이 들어오면 CoPopuDensityAPI 함수 호출
    path("copop/<str:s_day>/", CoPopuDensityOneAPI)
]

