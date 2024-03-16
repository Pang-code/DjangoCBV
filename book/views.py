from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps

MY_APP_VERSION = apps.get_app_config('book').version
from book.apps import BookConfig


def version(request):
    # return HttpResponse(MY_APP_VERSION)
    return HttpResponse(BookConfig.version)


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
from .serializers import BookSerializers, BaseSerializers, BookUpdateSerializers


class BookViewToModels(APIView):
    def get(self, request):
        book_list = BookInfo.objects.all()
        print(book_list)
        # book_list模型类 需要序列化
        # instance 序列化, data 反序列化  many 是否多个模型类
        serializers = BookSerializers(instance=book_list, many=True)
        print(serializers)
        print(serializers.data)
        # return HttpResponse(serializers.data)  #django自带的响应类 有序列表OrderedDict
        return Response(serializers.data)  # json 数据

    def post(self, request):
        # 反序列化
        print(request.data)
        # 构建序列化对象
        serializer = BaseSerializers(data=request.data)
        # 校验数据
        if serializer.is_valid():  # 通过返回true
            # new_book=Book.objects.create(**serializer.validated_data) #
            # serializer.save(serializer.data)
            serializer.save()  # serializer.validated_data  校验通过的数据
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BookDetailViewToModels(APIView):
    def get(self, request, id):
        book = BookInfo.objects.get(pk=id)
        serializer = BookSerializers(instance=book, many=False)  # many 一个 False
        return Response(serializer.data)

    def put(self, request, id):
        # 获取
        print(request.data)  # 请求参数
        update_book = BookInfo.objects.get(pk=id)  # 获取数据库准备修改的数据
        # 校验
        serializer = BookUpdateSerializers(instance=update_book, data=request.data)
        # 校验数据
        if serializer.is_valid():  # 通过返回true
            # Book.objects.filter(pk=id).update(**serializer.validated_data)
            # # return Response(serializer.data)  serializer instance 是更新之前的
            # updated_book = Book.objects.get(pk=id)
            # serializer.instance = updated_book
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, b_id):
        BookInfo.objects.get(pk=b_id).delete()
        return Response()
#
