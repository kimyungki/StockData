from django.shortcuts import render

from django.http import HttpResponse

import json

# Create your views here.

def index(request):

    return render(request, 'StockData/index.html')

#삼성전자
def output(request):
    line_counter = 0
    header = []
    customer_list = []
    i=0
    file = open("A000660_candle.csv", "r")
    for line in file:
        #customer_list.append(line.split(','))
        customer_list.append(line.strip('\n'))
        line_counter = line_counter + 1
    del customer_list[0]
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")


#네이버
def output2(request):
    line_counter = 0
    header = []
    customer_list = []
    file = open("netflix.csv", "r")
    for line in file:
        print()
        customer_list.append(line.strip('\n'))
    print(customer_list)
    return HttpResponse(json.dumps(customer_list), content_type="application/json")


#sk하이닉스
def output3(request):
    line_counter = 0
    header = []
    customer_list = []
    file = open("stock3.csv", "r")
    for line in file:
        print()
        customer_list.append(line.strip('\n'))

    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#삼성전자 예측
def predict(request):
    line_counter = 0
    test1_counter = 0
    test2_counter = 0
    i = 0
    header = []
    customer_list = []
    now = []
    pre = []
    file = open("test1.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1

    file2 = open("test2.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1

    customer_list.append(now)
    customer_list.append(pre)
    print("들어옴")
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

#네이버 예측
def predict2(request):
    line_counter = 0
    test1_counter = 0
    test2_counter = 0
    i = 0
    header = []
    customer_list = []
    now = []
    pre = []
    file = open("test1.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1

    file2 = open("test2.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1

    customer_list.append(now)
    customer_list.append(pre)
    print("들어옴(네이버)")
    return HttpResponse(json.dumps(customer_list), content_type="application/json")

def predict3(request):
    line_counter = 0
    test1_counter = 0
    test2_counter = 0
    i = 0
    header = []
    customer_list = []
    now = []
    pre = []
    file = open("test1.csv", "r")
    for line in file:
        now.append(line.strip('\n'))
        test1_counter = test1_counter + 1

    file2 = open("test2.csv", "r")
    for line in file2:
        pre.append(line.strip('\n'))
        test2_counter = test2_counter + 1

    customer_list.append(now)
    customer_list.append(pre)
    print(customer_list)
    print("들어옴(sk하이닉스)")
    return HttpResponse(json.dumps(customer_list), content_type="application/json")