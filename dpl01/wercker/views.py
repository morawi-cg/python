from django.shortcuts import render
# Create your views here.
def detail(request, question_id):
    return HttpResponse("wercker Account Credentials %s." % question_id)
