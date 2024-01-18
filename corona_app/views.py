from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from .models import CoPopuDensity
from .serializers import CoPopuDensitySerializer
from rest_framework.generics import get_object_or_404


# Create your views here.
def index (request) :
    return render(request, 'corona_app/index.html' )
def graph_form(request) :
    copop = CoPopuDensity.objects.only('std_day')
    date_list = copop.unique()
    date_list = sorted(date_list)
    print(date_list)   
    return render(request, 'deep_app/graph_form.html', {'date_list':date_list} )


# @api_view : 데코레이터. 함수에 대한 스타일 표기
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world! 안녕")
    # HTML 템플릿 반환하지 않고 데이터를 반환해준다

@api_view(['GET', 'POST'])
def CoPopuDensityAPI(request):
    if request.method == "GET":
        copop = CoPopuDensity.objects.all()

        # 직렬화 : 파이썬 객체 -> JSON
        # 서버 -> 클라이언트
        serializer = CoPopuDensitySerializer(copop, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # POST 요청으로 받은 데이터 역 직렬화
        # 클라이언트 -> 서버
        # JSON 문자열 -> 파이썬 데이터 객체로 변환
        serializer = CoPopuDensitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /corona_app/copop/특정일(2022-12-01) 2022-12-01날짜에 대한 정보 반환
@api_view(['GET'])
def CoPopuDensityOneAPI(request, s_day):
    # 특정일 정보 조회. 날짜 매개변수 필요
    copop = CoPopuDensity.objects.filter(std_day=s_day)
    serializer = CoPopuDensitySerializer(copop, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)     


