from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from . forms import SubjectSelectForm
from cards import models
import random
# Create your views here.


class SubjectSelectFormView(View):
    form_class = SubjectSelectForm
    template_name = 'study/select_subject.html'

    def get(self, request):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form':form})


    def post(self, request):
        #form = self.form_class(request.POST)
        return render(request, 'study/temp.html' )

'''       if form.is_valid():
            subject = form.cleaned_data['select_subject']
            count = len(models.Card.objects.filter(subject_id=subject))
            if count>= 20:

                cards = models.Card.objects.filter(subject_id=subject, next_turn_no__lte=subject.quiz_count)
                count = len(cards)
                cards = list(cards)
                final_cards = list()
                for i in range(0,20): final_cards.append(cards[random.randint(0,count)])

                context = {'cards' : final_cards}'''






