from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    no_of_cards = models.PositiveIntegerField(default=0)
    subject_rating = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    quiz_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return (self.name)


class Card(models.Model):

    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    card_id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    current_rating = models.PositiveIntegerField(default=0)
    previous_rating = models.PositiveIntegerField(default=0)
    no_of_turns_to_be_skipped = models.PositiveIntegerField(default=0)
    next_turn_no = models.PositiveIntegerField(default=0)