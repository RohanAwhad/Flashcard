from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import View
from django.views import generic
from .models import Subject, Card
from .forms import SubjectForm, CardForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from rest_framework import views, response, status
from .serializers import SubjectSerializer, CardSerializer


#api/subject
class SubjectList(views.APIView):

        def get(self, request):
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return response.Response(serializer.data)

        def post(self, request):
            pass


#api/cards
class CardList(views.APIView):

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        pass


class IndexView(generic.ListView):
    template_name = 'cards/index.html'

    def get_queryset(self):
        return Subject.objects.filter(user_id=self.request.user)


class SubjectCreateView(View):
    form_class = SubjectForm
    template_name = 'cards/subject_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user_id = request.user
            name = form.cleaned_data['name']
            model = Subject
            subject = model.objects.create(user_id = user_id, name = name)
            return redirect('cards:detail', subject.subject_id)


class SubjectUpdate(UpdateView):
    model = Subject
    fields = ['name']
    success_url = reverse_lazy('cards:index')


class SubjectDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('cards:index')


class DetailView(generic.DetailView):
    model = Subject
    template_name = 'cards/details.html'


class CardCreateView(View):
    form_class = CardForm
    template_name = 'cards/card_form.html'

    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request, pk):
        form = self.form_class(request.POST)

        if form.is_valid():
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            model = Card
            subject = Subject.objects.get(subject_id=self.kwargs['pk'])
            subject.no_of_cards += 1
            subject.save()
            model.objects.create(subject_id=subject, question=question, answer=answer)
            return redirect('cards:detail', subject.subject_id)


class CardUpdate(generic.UpdateView):
    model = Card
    template_name = 'cards/card_form.html'
    fields = ['question', 'answer']

    def get_success_url(self):
        return reverse_lazy('cards:detail', kwargs={'pk':self.kwargs['fk']})


class CardDelete(View):


    def get(self, request, fk, pk):
        return render(request, 'cards/card_confirm_delete.html', {'fk':fk})


    def post(self, request, fk, pk):
        card = Card.objects.get(card_id=pk)
        card.delete()
        subject = Subject.objects.get(subject_id=fk)
        subject.no_of_cards -= 1
        subject.save()
        return redirect('cards:detail', subject.subject_id)