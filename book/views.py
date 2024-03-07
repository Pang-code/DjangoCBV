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
