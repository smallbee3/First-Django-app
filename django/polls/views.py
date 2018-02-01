from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from polls.models import Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'index.html')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    test = {'test1': '박보영', 'test2': '아이유'}
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'test': test
    }
    return render(request, 'polls/index.html', context)


# part 3 - 1

def detail(request, question_id):

    # 1단계
    # return HttpResponse("You're looking at question %s." % question_id)

    # 2단계 try ~ except 방법
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # 3단계 get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
