from django.contrib.auth.models import User
from django.db import models

QUESTIONS = [
    {
        'likes': 5,
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answer_number': question_id * question_id,
        'tags': ['tag' for i in range(question_id)],
        'photos': f"img/Avatar{question_id}.jpg",
    } for question_id in range(12)
]

ANSWERS = [
    {
        'photos': f"img/Avatar{answer_id}.jpg",
        'id': answer_id,
        'likes': 5,
        'text': f'Text of answer #{answer_id}',
    } for answer_id in range(12)
]

HOTQUESTIONS = [
    {
        'likes': 5,
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answer_number': question_id * question_id,
        'photos': f"img/Avatar{question_id}.jpg",
    } for question_id in range(6)
]

TAGS = [
    {
        'id': tag_id,
        'title': f'Tag #{tag_id}',
    } for tag_id in range(3)
]


class Tag(models.Model):
    name = models.CharField(max_length=15)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)


class Like(models.Model):
    number = models.IntegerField()


class Answer(models.Model):
    text = models.TextField()
    models.ForeignKey(Profile, related_name='profile_related', on_delete=models.CASCADE)
    like = models.OneToOneField(Like, on_delete=models.CASCADE)


class QuestionManager(models.Manager):
    def get_hot_questions(self):
        return self.filter(status__exact='h')

    def get_new_questions(self):
        return self.objects.order_by('date')

    def get_tagged_questions(self, tag):
        return self.filter(tag__exact=tag)


class Question(models.Model):
    title = models.CharField(max_length=60)
    tag = models.ManyToManyField(Tag)
    text = models.TextField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    like = models.OneToOneField(Like, on_delete=models.CASCADE)
    models.ForeignKey(Profile, related_name='profile_related', on_delete=models.CASCADE)

    HOT = 'h'
    NORMAL = 'n'
    STATUSES = [
        (HOT, 'hot'),
        (NORMAL, 'ok')
    ]

    status = models.CharField(max_length=1, choices=STATUSES)
    date = models.DateTimeField(blank=True, null=True)

    objects = QuestionManager
