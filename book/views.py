from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def book(request):
    """
    fbv
    :param request:
    :return:
    """
    if request.method == "GET":
        return HttpResponse("get method")
    else:
        return HttpResponse("other method")


class BookView(View):
    """
    cbv基础写法
    """

    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")

    def put(self, request):
        return HttpResponse("put")

    def delete(self, request):
        return HttpResponse("del")


from rest_framework.views import APIView


class BookAPIView(APIView):
    """
    cbv REST APIVIEW
    """

    def get(self, request):
        print("query参数：", request.query_params)

        return HttpResponse("get APIView")

    def post(self, request):
        print("body参数：", request.data)
        return HttpResponse("post APIView")

    def put(self, request):
        print("原生view request :", request._request)
        print("原生view request path:", request._request.path)
        print("原生view request body:", request._request.body)
        print("原生view request method:", request._request.method)
        return HttpResponse("put APIView")

    def delete(self, request):
        return HttpResponse("del APIView")


from .models import BookInfo
from rest_framework.response import Response
from .serializers import BookSerializers


class BookViewToModels(APIView):
    def get(self, request):
        book_list = BookInfo.objects.all()
        # book_list模型类 需要序列化
        # instance 序列化, data 反序列化  many 是否多个模型类
        serializers = BookSerializers(instance=book_list, many=True)
        print(serializers.data)
        # return HttpResponse(serializers.data)  #django自带的响应类 有序列表OrderedDict
        return Response(serializers.data)  # json 数据

    def post(self, request):
        pass