from django.http.response import HttpResponse
from django.shortcuts import render

from mydata.models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response


# Create your views here.


# def search_phrase(request):
class Current_PairAPIView(APIView):
    def post(self, request, format=None):
        try:
            phrase = request.headers.get('query',None)
            print(phrase)
            # phrase='''(name eq amit) AND (roll gt 20) OR (roll lt 10))'''
            phrase=phrase.split('(')




            def parse_search_phrase(phrase):
                phrase='''(name eq amit) AND (roll gt 20) OR (roll lt 10))'''
                phrase2=phrase.split(" ")

                num=0
                query = Q()

                dummy=""

                for j in phrase2:
                    num=num+1
                    if num==1:
                        dummy =dummy+"Q"+j
                    if num==2:
                        dummy=dummy+j
                    if num==3:
                        dummy=dummy+j
                        print(dummy)
                    if num==4:
                        dummy=dummy+" "+j+" "
                        num=0
                
                dummy=dummy.replace("eq","=").replace("AND","&").replace("OR","|").replace("lt","__lt=").replace("gt","__gt=")
                dummy=dummy.replace("fi__lt=er","filter").replace("))",")")

                queryset = "Student.objects.filter(" +dummy+")"



                return queryset

            res=parse_search_phrase(phrase)

            return Response(res)
        except:
            return Response("Please enter a valid parameter in the header")
