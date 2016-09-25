from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
# from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import *
# Create your views here.
# def index(request):
#     latest_question_list = Qusetions.objects.order_by('-pub_date')[:5]
#     return render(request, 'polls/index.html', {'question_list': latest_question_list})


# def detail(request, question_id):
#     question = get_object_or_404(Qusetions, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You are looking at questinon %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Qusetions, pk=question_id)
#     # return HttpResponse("You are looking at the results of question %s." % question_id)
#     return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Qusetions.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Qusetions
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Qusetions
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Qusetions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.voted += 1
        selected_choice.save()
    # return HttpResponse("You are voting on question %s." % question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

