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
