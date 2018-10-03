import logging

from django.core import serializers
from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views import View
from . forms import SubjectSelectForm
from cards import models

import random
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

# Create your views here.

'''
def upload_rating(request):
    id = request.GET.get()
    return JsonResponse(data)'''

class SubjectSelectFormView(View):
    form_class = SubjectSelectForm
    template_name = 'study/select_subject.html'

    def get(self, request):
        form = self.form_class( user=request.user)
        return render(request, self.template_name, {'form':form})


    def post(self, request):
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            subject = models.Subject.objects.get(name=form.cleaned_data['name'], user_id=request.user)

            return redirect('study:quiz', subject.subject_id)
        else:
            return render(request, self.template_name, {'form':form})



def quiz(request, pk):
    subject = models.Subject.objects.get(subject_id=pk)
    count = len(models.Card.objects.filter(subject_id=subject))
    if count >= 20:
        cards = models.Card.objects.filter(subject_id=subject, next_turn_no__lte=subject.quiz_count)
        count = len(cards)
        cards = list(cards)
        final_cards = list()
        for i in range(0, 20):
            j = random.randint(0, count-1)
            final_cards.append(cards[j])
        data = serializers.serialize('json' , final_cards, cls=DjangoJSONEncoder)
        data = json.dumps(data)
        return render(request, 'study/quiz.html', content_type=json,context={'data':data})


'''

            logger = logging.getLogger(__name__)
            logger.error(j)

        final_cards_json = json.dumps(final_cards)
'''



