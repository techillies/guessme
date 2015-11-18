import random
import json
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from datetime import date, datetime
from words.models import *
# Create your views here.

def add_words(request):
    if request.method == "GET":
        words = Words.objects.all()
        return render_to_response("words/addwords.html",
                                  {'words':words },
                                  context_instance=RequestContext(request))
    elif request.method == "POST":
        name = request.POST.get("name")
        subword1 = request.POST.get("subword1")
        subword2 = request.POST.get("subword2")
        subword3 = request.POST.get("subword3")
        subword4 = request.POST.get("subword4")
        subword5 = request.POST.get("subword5")

        if Words.objects.filter(name=name).exists():
            print "word exist"

        else:
            wordsobj = Words.objects.create(name = name,
                                         subword1 = subword1,
                                         subword2 = subword2,
                                         subword3 = subword3,
                                         subword4 = subword4,
                                         subword5 = subword5
                                        )

            print "Store has been created successfully"
        return render_to_response("words/addwords.html",
                                  context_instance=RequestContext(request))

def guessme(request):
    if request.method == "GET":
        wordcount = Words.objects.count()
        pk = random.randint(1,wordcount)
        print "oblects comuts",wordcount
        if Words.objects.filter(pk=pk).exists():
            words = Words.objects.get(pk=pk)
        else:
            print "words does not exist!"

    return render_to_response("words/guessme.html",
                              {'words':words , 'wordcount':wordcount},
                                  context_instance=RequestContext(request))

def getnextword(request):
    print "hello1"
    if request.method == "GET":
        print "hello"
        nextwordpk = request.GET['randompk']
        print nextwordpk
        if Words.objects.filter(pk=nextwordpk).exists():
            words = Words.objects.get(pk=nextwordpk)
            nextworddetails = {
                'name' : words.name,
                'subword1':words.subword1,
                'subword2':words.subword2,
                'subword3':words.subword3,
                'subword4':words.subword4,
                'subword5':words.subword5
            }
            print nextworddetails
            words.save()
            return HttpResponse(json.dumps(nextworddetails), content_type="application/json")

        else:
            print "words does not exist!"



