from django.db import models

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answer_number': question_id*question_id,
        'tags': ['tag' for i in range(question_id)],
        'photos': f"img/Avatar{question_id}.jpg",
    }for question_id in range(10)
]

HOTQUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answer_number': question_id*question_id,
        'tags': ['tag' for i in range(question_id)],
        'photos': f"img/Avatar{question_id}.jpg",
    }for question_id in range(6)
]